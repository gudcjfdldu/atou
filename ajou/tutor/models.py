from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    name = models.CharField(blank=False, max_length=10)
    user = models.OneToOneField(User)
    number = models.CharField(blank=False, max_length=10)
    major = models.CharField(blank=False, max_length=10)
    email = models.EmailField(blank=False)
    
    def __unicode__(self):
        return self.user.username

    def update(self, username, number, email):
        self.user.username = username
        self.number = number
        self.email = email
        self.save()


# Create your models here.
