from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=25,blank=False)
    qualification = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.name