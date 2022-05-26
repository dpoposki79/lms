from rest_framework import serializers
from .models import Instructors, Students, Courses, Trainings

class InstructorsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Instructors
        fields = "__all__"

    def create(self, validated_data):  
        return Instructors.objects.create(**validated_data)


class StudentsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields = "__all__"

    def create(self, validated_data):  
        return Students.objects.create(**validated_data)

class TrainingsSerilizer(serializers.ModelSerializer):
    Instructor = InstructorsSerilizer(read_only=True)       #Ova se stava dokolku sakame da povrzeme podatoci. Pri API za pregledi ke dade detali i za doktori i za pacientot
    Student = StudentsSerilizer(read_only=True)
    class Meta:
        model=Trainings
        fields = "__all__"
        
    def create(self, validated_data):
        return Trainings.objects.create(**validated_data)

class CoursesSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields = "__all__"

    def create(self, validated_data):  
        return Courses.objects.create(**validated_data)