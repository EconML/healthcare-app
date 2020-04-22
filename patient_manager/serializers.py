from rest_framework import serializers
from .models import Condition, Patient, Servicerequest, Clinicalmeasures

class ClinicalmeasuresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Clinicalmeasures

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Condition

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Patient

class ServicerequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Servicerequest
