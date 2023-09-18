from django.db import models

# Create your models here.
class Lead(models.Model):
    
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

class Agent(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)