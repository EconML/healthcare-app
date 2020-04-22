from django.urls import path

from .views import ConditionListView, ConditionDetail, PatientList, PatientDetail, ServicerequestList, ServicerequestDetail, ClinicalmeasuresList, ClinicalmeasuresDetail

urlpatterns = [
    path('condition/', ConditionListView.as_view(), name='condition_list'),
    path('condition/<str:pk>/', ConditionDetail.as_view(), name='condition_detail'),
    path('patient/', PatientList.as_view(), name='patient_list'),
    path('patient/<str:pk>/', PatientDetail.as_view(), name='patient_detail'),
    path('servicerequest/', ServicerequestList.as_view(), name='servicerequest_list'),
    path('servicerequest/<str:pk>/', ServicerequestDetail.as_view(), name='servicerequest_detail'),
    path('clinicalmeasures/', ClinicalmeasuresList.as_view(), name='clinicalmeasures_list'),
    path('clinicalmeasures/<str:pk>/', ClinicalmeasuresDetail.as_view(), name='clinicalmeasures_detail'),
]
