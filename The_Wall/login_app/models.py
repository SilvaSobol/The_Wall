from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from datetime import datetime
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # PASS tests whether a field matches the pattern            
            errors.append ("Invalid email address!")

        if len(postData['first_name']) < 2:
            errors.append("First name should be at least 2 characters long ")

        if len(postData['last_name']) < 2:
            errors.append("Last name should be at least 2 characters long ")

        if len(postData['email']) < 1:    #pass email cant be blank 
            errors.append("Invalid Email")
        
        if len(postData['psw']) < 8:  
           errors.append("Your password needs to be at least 8 characters long")
        
        if postData['psw'] != postData['confirm']:      #PASS if password does not match 
            errors.append("Password does not match!")

        result = User.objects.filter(email = postData['email']) #PASS if the email already exists!
        if result:
            errors.append("Email already created!")


        else:                                                                   #PASS if younger than 13
            bd = datetime.strptime(postData['bday'],'%Y-%m-%d')
            today = datetime.now()
            if (bd.year +13, bd.month, bd.day) > (today.year, today.month, today.day):
               errors.append('User must be at least 13 years old to register')

            return errors


class User(models.Model):
    first_name = models.CharField(max_length = 55)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class WallMessage(models.Model):
    message = models.TextField(max_length=450)
    creator = models.ForeignKey(User, related_name = "user_messages", on_delete= models.CASCADE)
    user_likes = models.ForeignKey(User, related_name= "user_likes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(max_length= 300)
    wall_message = models.ForeignKey(WallMessage, related_name="wall_comments", on_delete= models.CASCADE)
    creator = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
