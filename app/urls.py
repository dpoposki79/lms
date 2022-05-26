from django.urls import path
from .views import InstructorView, StudentView, TrainingView, CourseView, Home

urlpatterns=[

    path("instruktor/", InstructorView.as_view()),
    path("student/", StudentView.as_view()),
    path("course/", CourseView.as_view()),
    path("training/", TrainingView.as_view()),

#    path ("github/", GithubConnect.as_view),
#    path ("github/auth/", github_views.oauth2_login),
#    path ("homepage/", home, name="home"),
    path('', Home.as_view(), name='home')



]