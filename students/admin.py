from django.contrib import admin
from .models import Student
from .models import Course

# Register Student model in Django Admin
admin.site.register(Student)

admin.site.register(Course)