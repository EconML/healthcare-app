from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics

from .models import Condition, Patient, Servicerequest, Clinicalmeasures
from .serializers import ConditionSerializer, PatientSerializer, ServicerequestSerializer, ClinicalmeasuresSerializer

class ClinicalmeasuresList(generics.ListCreateAPIView):
    queryset = Clinicalmeasures.objects.all()
    serializer_class = ClinicalmeasuresSerializer

class ClinicalmeasuresDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinicalmeasures.objects.all()
    serializer_class = ClinicalmeasuresSerializer

class ConditionListView(generics.ListCreateAPIView):
    queryset= Condition.objects.all()
    serializer_class = ConditionSerializer

class ConditionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class ServicerequestList(generics.ListCreateAPIView):
    queryset = Servicerequest.objects.all()
    serializer_class = ServicerequestSerializer

class ServicerequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servicerequest.objects.all()
    serializer_class = ServicerequestSerializer
