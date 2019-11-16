from django.db import models

# Create your models here.

class Movies(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	tags = models.CharField(max_length=20)
	image=models.FilePathField(path="/img")
	