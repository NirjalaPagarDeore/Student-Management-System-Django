from django import forms
from .models import Student
from .models import Course

# ==========================================
# Student Form
# ModelForm automatically creates a form
# based on the Student model.
# ==========================================

from django import forms
from .models import Student

# Student Form
class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = "__all__"

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "age": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "course": forms.Select(attrs={
             "class": "form-control"
            }),

             "email": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "photo": forms.FileInput(attrs={
            "class" : "form-control"
             }),
        }


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = "__all__"

        widgets = {

            "course_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "fee": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "duration": forms.TextInput(attrs={
                "class": "form-control"
            }),

        }