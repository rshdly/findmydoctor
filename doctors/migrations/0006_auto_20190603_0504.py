# Generated by Django 2.2 on 2019-06-02 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_auto_20190603_0503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='user_email',
            new_name='email',
        ),
    ]
