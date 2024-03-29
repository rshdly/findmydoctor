# Generated by Django 2.2 on 2019-06-02 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20190603_0454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='email',
            new_name='doctor_email',
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_email',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
