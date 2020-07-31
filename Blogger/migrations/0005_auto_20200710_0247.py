# Generated by Django 3.0.8 on 2020-07-10 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogger', '0004_auto_20200710_0156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['post_title']},
        ),
        migrations.AddField(
            model_name='tags',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
