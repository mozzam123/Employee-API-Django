from rest_framework import serializers
from .models import *

class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = "__all__"

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    addressDetails = AddressDetailsSerializer()
    workExperience = WorkExperienceSerializer(many=True)
    qualifications = QualificationSerializer(many=True)
    projects = ProjectSerializer(many=True)

    class Meta:
        model = UserModel
        fields = "__all__"
