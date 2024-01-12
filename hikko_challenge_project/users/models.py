from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    
    #Para acomodar el formato de los json de entrada, aunque debería ser un ManyToMany
    users_following = ArrayField(base_field=models.CharField(max_length=10))