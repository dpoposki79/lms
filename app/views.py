from django.shortcuts import render, redirect
from .models import Instructors, Students, Trainings, Courses
from rest_framework.response import Response
from .serializers import InstructorsSerilizer, StudentsSerilizer, TrainingsSerilizer, CoursesSerilizer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import SocialLoginView

from django.views.generic import TemplateView
# Create your views here.

class InstructorView(APIView):
    permission_classes = (IsAuthenticated,) #za najava t.e. logiranje
#zemanje podatoci samo za eden doktor
    def get (self, request):
        instructor=Instructors.objects.get(id=request.GET["instructorId"])
        instructor_serializer = InstructorsSerilizer(instructor)
        return Response(instructor_serializer.data)

    def post (self, request):
        instructor_serializer = InstructorsSerilizer(data=request.data)
        if instructor_serializer.is_valid():
            instructor_serializer.save()
            return Response(instructor_serializer.data, status=status.HTTP_201_CREATED)
        return Response ({"Info" : "Nastana greska"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        instructor = Instructors.objects.get(id=request.GET["instructorId"])
        instructor.delete()
        return Response ({"Info" : "Instruktorot e izbrisan"})

    def patch(self, request):
        instructor = Instructors.objects.get(id = request.data['id'])
        instructor_serializer = InstructorsSerilizer(instructor, data=request.data)
        if instructor_serializer.is_valid():
            instructor_serializer.save()
            return Response (instructor_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Errors": instructor_serializer.errors})
    

class StudentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get (self, request):
        student=Students.objects.get(id=request.GET["studentId"])
        student_serializer = StudentsSerilizer(student)
        return Response(student_serializer.data)

    def post (self, request):
        student_serializer = StudentsSerilizer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        return Response ({"Info" : "Nastana greska"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        student = Students.objects.get(id=request.GET["studentId"])
        student.delete()
        return Response ({"Info" : "Studentot e izbrisan"})

    def patch(self, request):
        student = Students.objects.get(id = request.data['id'])
        student_serializer = StudentsSerilizer(student, data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response (student_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Errors": student_serializer.errors})

class CourseView(APIView):
    permission_classes = (IsAuthenticated,)

    def get (self, request):
        course=Courses.objects.get(id=request.GET["courseId"])
        course_serializer = CoursesSerilizer(course)
        return Response(course_serializer.data)

    def post (self, request):
        course_serializer = CoursesSerilizer(data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data, status=status.HTTP_201_CREATED)
        return Response ({"Info" : "Nastana greska"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        course = Courses.objects.get(id=request.GET["courseId"])
        course.delete()
        return Response ({"Info" : "Kursot e izbrisan"})

    def patch(self, request):
        course = Courses.objects.get(id = request.data['id'])
        course_serializer = CoursesSerilizer(course, data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response (course_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Errors": course_serializer.errors})

class TrainingView(APIView):
    permission_classes = (IsAuthenticated,)

    def get (self, request):
        training=Trainings.objects.get(id=request.GET["trainingId"])
        training_serializer = TrainingsSerilizer(training)
        return Response(training_serializer.data)

    def post (self, request):
        training_serializer = TrainingsSerilizer(data=request.data)
        if training_serializer.is_valid():
            training_serializer.save()
            return Response(training_serializer.data, status=status.HTTP_201_CREATED)
        return Response ({"Info" : "Nastana greska"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        training = Trainings.objects.get(id=request.GET["trainingId"])
        training.delete()
        return Response ({"Info" : "Kursot e izbrisan"})

    def patch(self, request):
        training = Courses.objects.get(id = request.data['id'])
        training_serializer = TrainingsSerilizer(training, data=request.data)
        if training_serializer.is_valid():
            training_serializer.save()
            return Response (training_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Errors": training_serializer.errors})
 
def github_callback(request):
    return redirect ("http://127.0.0.1:8000/homepage")

def home(request):
    return Response({"Info" : "dobro e"})

class Home(TemplateView):
    template_name = "home.html"
