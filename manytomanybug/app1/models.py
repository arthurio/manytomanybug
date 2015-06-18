from django.db import models
from manytomanybug.app2.models import Upload

class FormA(models.Model):
    name = models.TextField()
    signature = models.ManyToManyField(Upload, related_name="+")

class FormB(models.Model):
    name = models.TextField()
    signature = models.ManyToManyField(Upload, related_name="+")

