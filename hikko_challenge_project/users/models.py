from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    
    #Para acomodar el formato de los json de entrada, aunque debería ser un ManyToMany
    users_following = models.JSONField(default=list)