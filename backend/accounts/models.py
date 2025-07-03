from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('employee', 'Employee')
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

class ManagerInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    manager_id = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.manager_id})"


class EmployeeInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    emp_id = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    manager = models.ForeignKey(ManagerInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.emp_id})"
