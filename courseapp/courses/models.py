from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


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
    image = models.ImageField(upload_to='category/%Y/%m', null=True, blank=True)
    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    categoryCourse = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='courses/%Y/%m', null=True, blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'categoryCourse')


class Lesson(BaseModel):
    subject = models.CharField(max_length=50, null=False)
    content = RichTextField(null=True)
    image = models.ImageField(upload_to='courses/%Y/%m', null=True, blank=True)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='lessons')

    class Meta:
        unique_together = ('subject', 'courses')

    def __str__(self):
        return self.subject


class Tag(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name
