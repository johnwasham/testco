from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    passwd = models.CharField(max_length=100)
    salt = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated every time the row is saved (INSERT or UPDATE)
    last_modified = models.DateTimeField(auto_now=True)

