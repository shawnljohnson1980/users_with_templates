from . import views
from django.urls import path


urlpatterns=[
    path('', views.index),
    path('view_super',views.view_super),
    path('view_villain',views.view_villain),
    path('view_teams',views.view_teams),
    path('create_super',views.create_super),
    path('supers_create',views.supers_create),
    path('team_create',views.team_create),
    path('create_team',views.create_team),

]