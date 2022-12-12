from django.views.generic import ListView
from django.shortcuts import render 
from django.db.models import Q
from django.db import connection

from . import models as my_models
from .models import *

# Create your views here.
def home_page(request):
    context = {}
    context['object_list'] = HomePage.objects.all()

    return render(request, 'vm_home_page.html', context=context)

class search_results(ListView):

    template_name = 'search.html'

    def get_queryset(self):
        table = getattr(my_models, self.request.GET.get('table'))
        query = self.request.GET.get('search')
        if hasattr(table, 'name'):
            object_list = table.objects.filter(Q(name__icontains=query))
        else:
            object_list = table.objects.filter(Q(id__icontains=query))

        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        table = getattr(my_models, self.request.GET.get('table'))
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['table'] = table

        if (hasattr(table, 'name')):
            context['attrs'] = [field.name for field in table._meta.fields if field.name != 'id'] 
        else:
            context['attrs'] = ['id']

        return context

def purchase_tickets_page(request):
    context = {}
    context['object_list'] = HomePage.objects.all()
    return render(request, 'purchase_tickets.html', context=context)

def purchase_tickets(request):
    #getting the information from form
    name = request.GET.get('fname')
    perfname = request.GET.get('shows')
    #getting information from the tables using the form information
    table = my_models.Attendees
    table2 = my_models.Performers
    table3 = my_models.Shows
    object_list = table.objects.filter(Q(name__icontains=name))[:1]

    attendee_id = object_list.get().id
    object_list2 = table2.objects.filter(Q(name__icontains=perfname))[:1]

    performer_id = object_list2.get().id
    object_list3 = table3.objects.filter(Q(id__icontains=performer_id))[:1]
    showid = object_list3.get().id
    print(f'showid: {showid}, performerid: {performer_id}, attendee_id: {attendee_id}')

#### ABOVE WORKS ####
# https://docs.djangoproject.com/en/4.1/topics/db/queries/
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/


#### BELOW IS STILL WRONG #### 


    #transaction for checking show availability
        #get capacity from shows table with show id
    obj_list = table3.objects.filter(Q(id__icontains=showid))[:1]
    capacity = obj_list.get().capacity
        #get count of tickets purchsed from Tickets table with show id
    table4 = my_models.Tickets
    obj_list2 = table4.objects.filter(Q(show_id__icontains=showid))
    numtix = obj_list2
        #check if capacity = num of tickets purchased, if yes, dont allow purchase

    #inserting row into tickets table
    #insert_row = Tickets(attendee_id=attendee_id, show_id=showid)
    #insert_row.save()

def reports_page(request):

    context = {};

    with connection.cursor() as cursor:
        cursor.execute("""SELECT p.name AS Name, avg(s.ticket_price) AS 'Average Ticket Price', count(s.id) AS 'Total Shows', sum(num_attendees) AS Fans FROM venue_manager_app_performers p 
                            JOIN venue_manager_app_shows s ON p.id = s.performer_id
		                    GROUP BY p.id;""")


        columns = [col[0] for col in cursor.description]
    
        performers_list = [dict(zip(columns, row)) for row in cursor.fetchall()]

        context['performers_list'] = performers_list
        context['performers_keys'] = performers_list[0].keys()

        cursor.execute("""SELECT v.name, COUNT(s.id) AS 'Total Shows', count(DISTINCT s.performer_id) AS 'Total Performers', avg(s.ticket_price) AS 'Average Ticket Price' FROM venue_manager_app_venues v
	                        JOIN venue_manager_app_shows s ON v.id = s.venue_id
                            GROUP BY v.id;""")

        columns = [col[0] for col in cursor.description]
    
        venues_list = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        context['venues_list'] = venues_list
        context['venues_keys'] = venues_list[0].keys()

    return render(request, 'report.html', context=context)
