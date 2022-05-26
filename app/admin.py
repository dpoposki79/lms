from django.contrib import admin
from .models import Instructors, Students, Trainings, Courses
# Register your models here.


admin.site.register(Instructors)
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Trainings)

class InstructorsAdmin(admin.ModelAdmin):
    list_display = ("id", "Ime", "Prezime", "Email", "Course")
    list_filter = ("Course",)
    search_fields = ("Course", "Ime", "Prezime")

class StudentsAdmin(admin.ModelAdmin):
    list_display = ("id", "Ime", "Prezime", "Email", "Course")
    list_filter = ("Course", "Homework")
    search_fields = ("Course", "Ime", "Prezime")