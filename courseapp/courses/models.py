from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    pass


class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    categoryCourse = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
