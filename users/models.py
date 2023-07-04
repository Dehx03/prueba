from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission

class User(AbstractUser):
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    phone_number = models.CharField(max_length=20)

    groups = models.ManyToManyField(Group, related_name='usuarios_personalizados')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_personalizados')