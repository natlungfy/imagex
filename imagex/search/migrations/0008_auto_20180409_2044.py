# Generated by Django 2.0.2 on 2018-04-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20180403_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagehastag',
            name='imgID',
        ),
        migrations.RemoveField(
            model_name='imagehastag',
            name='tagID',
        ),
        migrations.AddField(
            model_name='image',
            name='tag',
            field=models.ManyToManyField(to='search.Tag'),
        ),
        migrations.DeleteModel(
            name='ImageHasTag',
        ),
    ]