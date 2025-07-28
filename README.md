# ShadowWatch – Malicious URL Detection Using Machine Learning

ShadowWatch is a web-based malware detection system that identifies potentially harmful URLs using machine learning techniques. It classifies URLs as malicious or benign based on behavioral patterns and data features.

## 🔍 Project Overview

- **Goal**: Detect malicious URLs and display detection type using ML models.
- **Type**: Full-stack Django application.
- **Target Users**: General users and security administrators.
- **Detection Logic**: Based on dataset-driven ML classification of URLs.
- **Tech Stack**:  
  - **Backend**: Python, Django  
  - **Frontend**: HTML, CSS (basic)  
  - **ML/DS Libraries**: scikit-learn, NumPy, Pandas  
  - **Database**: SQLite  
  - **Platform**: Local + Render (for deployment)

## 💡 Features

- User and Admin modules
- Predict URL as malicious or benign
- Visualize detection statistics (likes/dislikes charts, detection ratio)
- Trained on real malware datasets
- Download predicted results
- User authentication, registration, and profile viewing

## 🧠 Machine Learning Flow

- Data cleaning using **Pandas** & **NumPy**
- ML models trained on `Malware_Datasets.csv`
- Output predictions shown with type classification
- Accuracy evaluated with various classification models

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/hari-chintaparthi/ShadowWatch
   cd ShadowWatch
   ```

2. Create virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start server:
   ```bash
   python manage.py runserver
   ```

6. Open browser: `http://127.0.0.1:8000/`

## 📁 Project Structure

```
Dark_TRACER_Early_Detection/
│
├── 📁 Dark_TRACER_Early_Detection/        # Main Django config and routing
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── 📁 Remote_User/                        # Handles user-side logic
│   ├── 📁 migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── 📁 Service_Provider/                   # Handles admin-side logic
│   ├── 📁 migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── 📁 Template/                           # Frontend HTML files and assets
│   ├── 📁 Ruser/
│   │   ├── design.html
│   │   ├── get_url_details.html
│   │   ├── login.html
│   │   ├── Predict_Detection_Type.html
│   │   ├── predict_form.html
│   │   ├── ratings.html
│   │   ├── Register1.html
│   │   └── ViewYourProfile.html
│   ├── 📁 Sprovider/
│   │   ├── charts.html
│   │   ├── charts1.html
│   │   ├── design1.html
│   │   ├── dislikeschart.html
│   │   ├── Download_Predicted_DataSets.html
│   │   ├── Find_Malware_Detection_Type_Ratio.html
│   │   ├── likeschart.html
│   │   ├── Predict_Malware_Detection_Type_Details.html
│   │   ├── serviceproviderlogin.html
│   │   ├── train_model.html
│   │   └── View_Remote_Users.html
│   └── 📁 images/
│       ├── bg.jpg
│       ├── Login.jpg
│       └── Register.jpg
│
├── 📁 Database/                           # DB helpers or raw data
├── Labeled_Data.csv                      # Cleaned/labeled dataset
├── Malware_Datasets.csv                  # Raw malware dataset
├── build.sh                              # Build or deploy script (optional)
├── manage.py                             # Django project manager
├── render.yaml.txt                       # Render platform config
├── requirements.txt                      # Python dependency file
└── .gitignore                            # Git ignore rules
```

## 🌐 GitHub Repository

🔗 [ShadowWatch on GitHub](https://github.com/hari-chintaparthi/ShadowWatch)
