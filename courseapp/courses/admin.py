from django.contrib import admin
from .models import Category,Course


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject']


admin.site.register(Category, CategoryAdmin)

admin.site.register(Course, CourseAdmin)
