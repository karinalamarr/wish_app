from django.db import models

class Users(models.Model):
    first_name=models.CharField(max_length=254)
    last_name=models.CharField(max_length=254)
    age=models.IntegerField(default=200)
    email_address=models.EmailField(max_length=254)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
