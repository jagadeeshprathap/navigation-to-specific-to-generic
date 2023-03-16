from app2.views import *
from django.urls import path
app_name='murali'
urlpatterns=[
    path('murali/',murali,name='murali'),
]