from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 60)
    occupants = models.ManyToManyField(User,blank=True,related_name='occupants_count')
    admin = models.ForeignKey(User,on_delete = models.CASCADE)

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_profile')
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 60)

class Business(models.Model):
    name = models.CharField(max_length = 60)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'business_user')
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE,related_name = 'business_neighbourhood')
    email = models.EmailField(max_length = 60)
