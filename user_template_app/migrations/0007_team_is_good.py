# Generated by Django 2.2.4 on 2021-04-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_template_app', '0006_auto_20210419_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_good',
            field=models.BooleanField(default=True),
        ),
    ]