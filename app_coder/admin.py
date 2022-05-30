from django.contrib import admin

from app_coder.models import Course, Entrenador, Student, Homework

admin.site.register(Course)

admin.site.register(Student)

admin.site.register(Entrenador)

admin.site.register(Homework)
