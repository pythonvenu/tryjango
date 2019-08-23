from django.db import models
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')

def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class Content(models.Model):
    name = models.CharField(max_length=200)
    #user = models.ForeignKey(User)
    file = models.FileField(upload_to=content_file_name)

class ItemDetails(models.Model):
    itemname = models.CharField(max_length=120)
    itemDesc = models.CharField(max_length=120)
    itemPrice = models.DecimalField(max_digits=5, decimal_places=2)

class Student(models.Model):
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=16, default="Male")
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "students"

class Marks(models.Model):
    student = models.ForeignKey(Student, related_name = "marks", on_delete=models.CASCADE)
    class_name = models.CharField(max_length=32)
    english = models.CharField(max_length=3)
    nepali = models.CharField(max_length=3)

    def __str__(self):
        return self.student

    class Meta:
        db_table = "marks"