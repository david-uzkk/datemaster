from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    image = models.ImageField(default='avatar.jpg', upload_to='Profile_Images')

    def __str__(self):
        return f'{self.staff.username}-Profile'
    