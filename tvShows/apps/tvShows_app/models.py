from __future__ import unicode_literals
from django.db import models

class ShowMananger(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
             errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releaseDate = models.DateTimeField()
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ShowMananger()