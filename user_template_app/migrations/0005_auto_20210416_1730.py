# Generated by Django 2.2.4 on 2021-04-16 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_template_app', '0004_auto_20210416_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_date',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='superhero',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='superheroes', to='user_template_app.Team'),
        ),
    ]
