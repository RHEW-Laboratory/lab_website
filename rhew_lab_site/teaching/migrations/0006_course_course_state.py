# Generated by Django 2.0.1 on 2018-01-15 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0005_auto_20180114_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_state',
            field=models.CharField(default='Previous Year', max_length=255),
        ),
    ]
