# serializers.py

from rest_framework import serializers
from .models import Address, WorkExperience, Qualification, Project, Employee

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    addressDetails = AddressSerializer()
    workExperience = WorkExperienceSerializer(many=True)
    qualifications = QualificationSerializer(many=True)
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('addressDetails')
        work_experience_data = validated_data.pop('workExperience')
        qualification_data = validated_data.pop('qualifications')
        project_data = validated_data.pop('projects')

        address_instance = Address.objects.create(**address_data)

        work_experience_instances = [WorkExperience.objects.create(**data) for data in work_experience_data]
        qualification_instances = [Qualification.objects.create(**data) for data in qualification_data]
        project_instances = [Project.objects.create(**data) for data in project_data]

        employee_instance = Employee.objects.create(addressDetails=address_instance, **validated_data)
        employee_instance.workExperience.set(work_experience_instances)
        employee_instance.qualifications.set(qualification_instances)
        employee_instance.projects.set(project_instances)

        return employee_instance
    
    def update(self, instance, validated_data):
        address_data = validated_data.pop('addressDetails', None)
        work_experience_data = validated_data.pop('workExperience', [])
        qualification_data = validated_data.pop('qualifications', [])
        project_data = validated_data.pop('projects', [])

        if address_data:
            address_instance = instance.addressDetails
            address_instance.hno = address_data.get('hno', address_instance.hno)
            address_instance.street = address_data.get('street', address_instance.street)
            address_instance.city = address_data.get('city', address_instance.city)
            address_instance.state = address_data.get('state', address_instance.state)
            address_instance.save()

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phoneNo = validated_data.get('phoneNo', instance.phoneNo)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()

        # Update work experiences
        instance.workExperience.all().delete()
        work_experience_instances = [WorkExperience.objects.create(employee=instance, **data) for data in work_experience_data]

        # Update qualifications
        instance.qualifications.all().delete()
        qualification_instances = [Qualification.objects.create(employee=instance, **data) for data in qualification_data]

        # Update projects
        instance.projects.all().delete()
        project_instances = [Project.objects.create(employee=instance, **data) for data in project_data]

        instance.workExperience.set(work_experience_instances)
        instance.qualifications.set(qualification_instances)
        instance.projects.set(project_instances)

        return instance
