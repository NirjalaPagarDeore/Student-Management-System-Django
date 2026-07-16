from django.db import models
import os

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    # New Field
    email = models.EmailField(null=True, blank=True)

    photo = models.ImageField(
    upload_to="students/",
    null=True,
    blank=True
)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):

        if self.pk:

            old_student = Student.objects.get(pk=self.pk)

            if old_student.photo != self.photo:

                if old_student.photo:

                    if os.path.isfile(old_student.photo.path):

                        os.remove(old_student.photo.path)

        super().save(*args, **kwargs)
    



