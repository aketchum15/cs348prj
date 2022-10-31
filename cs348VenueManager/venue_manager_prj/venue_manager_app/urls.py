from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('page2test.html', views.page2test, name='page2test'),
]
