# Generated by Django 2.2.7 on 2019-12-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(default='default.jpg', upload_to='blog_pics'),
        ),
    ]
