from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    word = models.CharField(max_length=255)
    definition = models.TextField()
    meaning = models.TextField() 
