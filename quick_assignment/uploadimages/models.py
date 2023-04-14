from django.db import models

# Create your models here.
class UserDetails(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='imgs')