from django.urls import path
from . import views

urlpatterns = [
    path('', views.testfunc, name='home_page'),
]
