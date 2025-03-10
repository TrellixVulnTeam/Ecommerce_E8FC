from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'Customer'
