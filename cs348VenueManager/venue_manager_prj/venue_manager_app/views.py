from django.views.generic import ListView
from django.shortcuts import render 
from django.db.models import Q

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
    name = request.GET('fname')
    perfname = request.GET('shows')
    #getting information from the tables using the form information
    table = my_models.Attendees.Meta.indexes
    table2 = my_models.Performers
    table3 = my_models.Shows
    object_list = table.objects.filter(Q(name__icontains=name))
    attendee_id = object_list[0]
    object_list2 = table2.objects.filter(Q(name__icontains=perfname))
    performer_id = object_list2[0]
    object_list3 = table3.objects.filter(Q(id__icontains=performer_id))
    show_id = object_list3[0]
    #inserting row into tickets table
    insert_row = Tickets(attendee_id=attendee_id, show_id=show_id)
    insert_row.save()
