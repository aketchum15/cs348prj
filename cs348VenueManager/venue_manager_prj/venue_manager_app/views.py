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
