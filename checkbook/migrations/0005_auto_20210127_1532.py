# Generated by Django 3.1.5 on 2021-01-27 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkbook', '0004_auto_20210127_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default=' -- ', on_delete=django.db.models.deletion.CASCADE, to='checkbook.category'),
        ),
    ]
