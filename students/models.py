from django.db import models

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
    



