# Generated by Django 2.2 on 2019-06-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_auto_20190603_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=15),
        ),
    ]
