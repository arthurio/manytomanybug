from django.db import models
from manytomanybug.app2.models import Upload

# Create your models here.
class FormA(models.Model):
    name = models.TextField()
    signature = models.ManyToManyField(Upload, related_name="+")

# Create your models here.
class FormB(models.Model):
    name = models.TextField()
    signature = models.ManyToManyField(Upload, related_name="+")



