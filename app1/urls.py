from app1.views import *
from django.urls import path
app_name='ramu'
urlpatterns=[
    path('ramu/',ramu,name='ramu'),
]