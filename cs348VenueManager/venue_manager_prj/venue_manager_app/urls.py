from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home page'),
    path('search/', views.search_results.as_view(), name='search results'),
    path('purchase_tickets/', views.purchase_tickets_page, name='purchase tickets page'),
    path('purchase_tickets/', views.purchase_tickets, name='purchase tickets'),
    path('reports/', views.reports_page, name='reports page')
]
