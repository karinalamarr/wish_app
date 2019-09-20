from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) <3 & len(postData['name']) < 5:
            errors["password"] = "Both first and last name should be at least 4 characters"
        # if postData['email'] !=
        return errors

class User(models.Model):
    first_ name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()