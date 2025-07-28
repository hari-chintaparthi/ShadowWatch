from django.urls import path, re_path
from django.contrib import admin
from Remote_User import views as remoteuser
from Dark_TRACER_Early_Detection import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^$', remoteuser.login, name="login"),
    re_path(r'^Register1/$', remoteuser.Register1, name="Register1"),
    re_path(r'^Predict_Detection_Type/$', remoteuser.Predict_Detection_Type, name="Predict_Detection_Type"),
    re_path(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),

    re_path(r'^Get_URL_Details/$', remoteuser.get_url_details, name='get_url_details'),
    re_path(r'^extracted_predict/$', remoteuser.extracted_predict, name='extracted_predict'),

    re_path(r'^serviceproviderlogin/$', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    re_path(r'^View_Remote_Users/$', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    re_path(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts, name="charts"),
    re_path(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),
    re_path(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    re_path(r'^Find_Malware_Detection_Type_Ratio/$', serviceprovider.Find_Malware_Detection_Type_Ratio, name="Find_Malware_Detection_Type_Ratio"),
    re_path(r'^train_model/$', serviceprovider.train_model, name="train_model"),
    re_path(r'^Predict_Malware_Detection_Type_Details/$', serviceprovider.Predict_Malware_Detection_Type_Details, name="Predict_Malware_Detection_Type_Details"),
    re_path(r'^Download_Predicted_DataSets/$', serviceprovider.Download_Predicted_DataSets, name="Download_Predicted_DataSets"),
    # path('predict/', remoteuser.Predict_Detection_Type, name='Predict_Detection_Type'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
