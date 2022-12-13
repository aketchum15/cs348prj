from django.views.generic import ListView
from django.shortcuts import render 
from django.db.models import Q
from django.db import connection
from django.contrib import messages

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
    #context = {}
    #context['object_list'] = HomePage.objects.all()
    return render(request, 'purchase_tickets.html')

def purchase_tickets(request):
    #getting the information from form
    fname = request.GET.get('fname')
    perfname = request.GET.get('shows')
    #getting information from the tables using the form information
    table = my_models.Attendees
    table2 = my_models.Performers
    table3 = my_models.Shows
    object_list = table.objects.filter(Q(name__icontains=fname))[:1]
    attendeeid = str(object_list.get().id)
    object_list4 = table2.objects.filter(Q(name__icontains=perfname))[:1]
    perf_id = object_list4.get().id
    #object_list2 = table3.objects.filter(Q(performer_id=perf_id))[:1]
    #ticketprice = object_list2.get().ticket_price
    object_list3 = table3.objects.filter(Q(performer_id=perf_id))[:1]
    showid = str(object_list3.get().id)
    print(f"show: {showid} attendee: {attendeeid}")


 #transaction for checking show availability

    #obj_list = table3.objects.filter(Q(id=showid))[:1]
    #capacity = obj_list.get().num_attendees

    #table4 = my_models.Tickets
    #obj_list2 = table4.objects.filter(Q(show_id=showid))
    #numtix = obj_list2.count()

    #if(capacity==numtix):
        #cannot buy tickets

    #else:
        #row = Tickets(show_id=showid, attendee_id=attendeeid, price=50)
        #row.save()


    with connection.cursor() as cursor:
        cursor.execute("""SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
                       START TRANSACTION; 
                       INSERT INTO venue_manager_app_tickets(show_id, attendee_id, price) VALUES(2, 2, 50);""")
        cursor.execute("SELECT venue_manager_app_shows.num_attendees, count(venue_manager_app_tickets.id) FROM venue_manager_app_tickets JOIN venue_manager_app_shows ON venue_manager_app_shows.id=venue_manager_app_tickets.show_id WHERE show_id=%s GROUP BY show_id;", [showid])
        val = cursor.fetchone()

        print("val: ", val)

        if(val==None):
            cursor.execute("ROLLBACK;")
            messages.error(request, 'There are no available tickets for this show, please select a different one')
        else:
            cursor.execute("COMMIT;")
            messages.success(request, "Success! Your tickets have been purchased!")




    return render(request, 'purchase_tickets.html')

def reports_page(request):

    context = {};

    with connection.cursor() as cursor:
        cursor.execute("""SELECT p.name AS Name, IFNULL(AVG(t.price), 0) AS 'Average Ticket Price', count(s.id) AS 'Total Shows', sum(num_attendees) AS Fans FROM venue_manager_app_performers p 
                            JOIN venue_manager_app_shows s ON p.id = s.performer_id
                            LEFT JOIN venue_manager_app_tickets t ON t.show_id = s.id
		                    GROUP BY p.id;""")


        columns = [col[0] for col in cursor.description]
    
        performers_list = [dict(zip(columns, row)) for row in cursor.fetchall()]

        context['performers_list'] = performers_list
        context['performers_keys'] = performers_list[0].keys()

        cursor.execute("""SELECT v.name, COUNT(s.id) AS 'Total Shows', count(DISTINCT s.performer_id) AS 'Total Performers', IFNULL(AVG(t.price), 0) AS 'Average Ticket Price' FROM venue_manager_app_venues v
	                        JOIN venue_manager_app_shows s ON v.id = s.venue_id
                            LEFT JOIN venue_manager_app_tickets t ON t.show_id = s.id
                            GROUP BY v.id;""")

        columns = [col[0] for col in cursor.description]
    
        venues_list = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        context['venues_list'] = venues_list
        context['venues_keys'] = venues_list[0].keys()

    return render(request, 'report.html', context=context)
