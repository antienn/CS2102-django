# Generated by Django 4.2.6 on 2023-10-29 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_lesson_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='courses',
        ),
    ]
