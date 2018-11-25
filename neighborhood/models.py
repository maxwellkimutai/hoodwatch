from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)
    admin = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_profile')
    first_name = models.CharField(max_length = 50,null=True)
    last_name = models.CharField(max_length = 50,null=True)
    bio = models.TextField(null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 60)

    def __str__(self):
        return self.user.username

class Business(models.Model):
    name = models.CharField(max_length = 60)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'business_user')
    description = models.CharField(max_length = 150,null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE,related_name = 'business_neighbourhood')
    category = models.ForeignKey('Category',on_delete = models.CASCADE,null=True)
    email = models.EmailField(max_length = 60)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE,null=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.comment

class Location(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name
