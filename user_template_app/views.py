from django.shortcuts import render,redirect
from .models import SuperHero, Team,Super_Villain
from django.contrib import messages
# Create your views here.
def index(request):

    context={
       ' supers':SuperHero.objects.all(),
       
       'team':Team.objects.all(),
      
    }
    return render(request,'index.html',context)


def view_super(request):
     context={
       'supers':SuperHero.objects.all(),
     }
     return render(request,'super_heroes.html',context)

def view_villain(request):
    context={
        'super_villains':Super_Villain.objects.all(),
    }
    return render(request, 'super_villains.html',context)

def view_teams(request):
    context={
        'teams':Team.objects.all(),
    }
    return render(request,'super_clubs.html',context)


def create_super(request):
    team=Team.objects.all()
    superhero=SuperHero.objects.all()
    real_name=request.POST['real_name']
    code_name=request.POST['code_name']
    team=request.POST['team']
    is_good=request.POST['is_good'] 
    SuperHero.objects.create(
        real_name=real_name,
        code_name=code_name,
       is_good=is_good,
       team=team
    )
    context={
       'supers':Team.objects.get(team_name)
     }
    messages.info(request, "Hero Created Successfully")
    return redirect('/view_super',context)

def create_villain(request):
     super_villain=Super_Villain.objects.all()
     real_name=request.POST['real_name']
     code_name=request.POST['code_name']
     is_good=request.POST['is_good']
     team=request.POST['team']
     Super_Villain.objects.create(
        real_name=real_name,
        code_name=code_name,
        is_good=is_good,
        team=team
    )
     messages.info(request, "Hero Created Successfully")
     return redirect('/view_super')

def supers_create(request):
    return render(request,'create_supers.html')

def team_create(request):
    team=Team.objects.all()
    context={
    'teams':Team.objects.all()
    }

    return render(request,'create_team.html',context)

def villain_create(request):
    return render(request,'create_supers.html')

def create_team(request):
    team=Team.objects.all()
    bad_team=Team.objects.filter(is_good=False)
    super_villains = bad_team
    team_name=request.POST['team_name']
    created_date=request.POST['created_date']
    is_good=request.POST['is_good']
    Team.objects.create(
        team_name=team_name,
        created_date= created_date,
        is_good=is_good
    )
    messages.info(request, "Hero Created Successfully")
    return redirect('/view_teams')
