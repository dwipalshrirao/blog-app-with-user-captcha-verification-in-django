# Generated by Django 3.1.1 on 2021-02-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(blank=True, choices=[('public', 'public'), ('private', 'private')], max_length=20, null=True),
        ),
    ]