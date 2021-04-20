from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Team(models.Model):
    team_name=models.CharField(max_length=45)
    created_date=models.CharField(max_length=50)
    is_good = models.BooleanField(default=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    

class SuperHero(models.Model):
    real_name=models.CharField(max_length=45)
    code_name=models.CharField(max_length=45)
    team=models.ForeignKey(Team, related_name="superheroes",on_delete=DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Super_Villain(models.Model):
    real_name=models.CharField(max_length=45)
    code_name=models.CharField(max_length=45)
    team=models.ForeignKey(Team,related_name='super_villians',on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)