
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from .models import *

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.user.username


# parent model
class forum(models.Model):
    TOPIC = (
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Antarctica', 'Antarctica'),
        ('Europe', 'Europe'),
        ('Oceania', 'Oceania'),
    )
    name = models.CharField(max_length=200, default="anonymous")
    email = models.CharField(max_length=200, null=True)
    topic = models.CharField(max_length=100, null=False, choices=TOPIC)
    description = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)







