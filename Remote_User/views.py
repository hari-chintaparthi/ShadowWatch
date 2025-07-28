from django.shortcuts import render, redirect, get_object_or_404
from urllib.parse import urlparse
import requests
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier

from Remote_User.models import ClientRegister_Model, detection_type, detection_ratio, detection_accuracy


# -------------------- AUTH & PROFILE --------------------

def login(request):
    if request.method == "POST" and 'submit1' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            enter = ClientRegister_Model.objects.get(username=username, password=password)
            request.session["userid"] = enter.id
            return redirect('ViewYourProfile')
        except:
            pass
    return render(request, 'RUser/login.html')


def Register1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        ClientRegister_Model.objects.create(
            username=username, email=email, password=password,
            phoneno=phoneno, country=country, state=state,
            city=city, address=address, gender=gender
        )
        return render(request, 'RUser/Register1.html', {'object': "Registered Successfully"})

    return render(request, 'RUser/Register1.html')


def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id=userid)
    return render(request, 'RUser/ViewYourProfile.html', {'object': obj})


# -------------------- URL FEATURE EXTRACTION --------------------

def extract_features_from_url(url):
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    https_token = 1 if "https" in url.lower() else 0
    length_url = len(url)
    length_hostname = len(hostname)

    try:
        response = requests.get(url, timeout=3)
        page_rank = 1 if response.status_code == 200 else 0
    except:
        page_rank = 0

    return length_url, length_hostname, https_token, page_rank


def get_url_details(request):
    return render(request, 'RUser/get_url_details.html')


def extracted_predict(request):  # used in your URL pattern
    if request.method == "POST":
        url = request.POST.get('url')
        length_url, length_hostname, https_token, page_rank = extract_features_from_url(url)

        # Store in session
        request.session['url'] = url
        request.session['length_url'] = length_url
        request.session['length_hostname'] = length_hostname
        request.session['https_token'] = https_token
        request.session['page_rank'] = page_rank

        return redirect('Predict_Detection_Type')
    return redirect('Get_URL_Details')


# -------------------- PREDICTION --------------------

def Predict_Detection_Type(request):
    if request.method == "POST" or all(k in request.session for k in [
        'url', 'length_url', 'length_hostname', 'https_token', 'page_rank'
    ]):
        url = request.POST.get('url') or request.session.get('url')
        length_url = int(request.POST.get('length_url') or request.session.get('length_url'))
        length_hostname = int(request.POST.get('length_hostname') or request.session.get('length_hostname'))
        https_token = int(request.POST.get('https_token') or request.session.get('https_token'))
        page_rank = int(request.POST.get('page_rank') or request.session.get('page_rank'))

        df = pd.read_csv('Malware_Datasets.csv', encoding='latin-1')
        df['Results'] = df['status'].apply(lambda s: 0 if s == "legitimate" else 1)

        X = df['url']
        y = df['Results']

        cv = CountVectorizer(lowercase=False, strip_accents='unicode', ngram_range=(1, 1))
        X = cv.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

        models = []

        NB = MultinomialNB()
        NB.fit(X_train, y_train)
        naivebayes = accuracy_score(y_test, NB.predict(X_test)) * 100
        models.append(('naive_bayes', NB))
        detection_accuracy.objects.create(names="Naive Bayes", ratio=naivebayes)

        lin_clf = svm.LinearSVC()
        lin_clf.fit(X_train, y_train)
        svm_acc = accuracy_score(y_test, lin_clf.predict(X_test)) * 100
        models.append(('svm', lin_clf))
        detection_accuracy.objects.create(names="SVM", ratio=svm_acc)

        reg = LogisticRegression(solver='lbfgs', max_iter=1000)
        reg.fit(X_train, y_train)
        models.append(('logistic', reg))

        dtc = DecisionTreeClassifier()
        dtc.fit(X_train, y_train)
        models.append(('DecisionTreeClassifier', dtc))

        kn = KNeighborsClassifier()
        kn.fit(X_train, y_train)
        models.append(('KNeighborsClassifier', kn))

        classifier = VotingClassifier(models)
        classifier.fit(X_train, y_train)

        vector = cv.transform([url]).toarray()
        predict_text = classifier.predict(vector)

        prediction = int(predict_text[0])
        result = 'legitimate' if prediction == 0 else 'malware'

        detection_type.objects.create(
            url=url,
            length_url=length_url,
            length_hostname=length_hostname,
            https_token=https_token,
            page_rank=page_rank,
            Prediction=result
        )

        return render(request, 'RUser/Predict_Detection_Type.html', {'objs': result})

    return render(request, 'RUser/Predict_Detection_Type.html')

# from django.shortcuts import redirect
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def process_url_and_predict(request):
#     if request.method == "POST":
#         url = request.POST.get('url')
#         request.session['url'] = url
#         request.session['length_url'] = len(url)
#         request.session['length_hostname'] = len(urlparse(url).netloc)
#         request.session['https'] = 1 if "https" in url else 0
#         request.session['pagerank'] = 5.3
#         return redirect('Predict_Detection_Type')
#     return redirect('Get_URL_Details')  # Or wherever you want to go for GET

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def process_url_and_predict(request):
#     if request.method == "POST":
#         url = request.POST.get('url')
#         # result = "Predict_Detection_Type"
#         return render(request, 'RUser/Predict_Detection_Type.html')
#     return render(request, 'RUser/Predict_Detection_Type.html')
