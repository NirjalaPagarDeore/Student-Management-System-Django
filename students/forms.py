from django import forms
from .models import Student


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

            "course": forms.TextInput(attrs={
                "class": "form-control"
            }),

             "email": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "photo": forms.FileInput(attrs={
            "class" : "form-control"
             }),
        }