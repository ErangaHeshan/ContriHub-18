# Generated by Django 2.1.2 on 2018-10-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0002_prs_pr_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='issues',
            name='label',
            field=models.IntegerField(default=1, verbose_name='label_of_issue'),
        ),
    ]
