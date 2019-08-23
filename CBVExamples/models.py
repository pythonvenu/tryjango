from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User

# CBV examples
class Article(models.Model):
    title	= models.CharField(max_length=120)
    content	= models.TextField()
    active	= models.BooleanField(default=True)

    def get_absolute_url(self):
        #return reverse('article:article-details', kwargs={"id": self.id})
        return reverse('article:create')

class Course(models.Model):
    title = models.CharField(max_length=200)