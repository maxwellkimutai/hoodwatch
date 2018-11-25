from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)
    admin = models.ForeignKey(User,on_delete = models.CASCADE)
    occupants = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood

    def update_neighborhood(self):
        self.save()

    def update_occupants(self):
        self.occupants += 1
        self.save()


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

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = Business.objects.get(id = business_id)
        return business

    def update_business(self):
        self.save()

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE)
    type = models.CharField(max_length = 50,null=True)
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
