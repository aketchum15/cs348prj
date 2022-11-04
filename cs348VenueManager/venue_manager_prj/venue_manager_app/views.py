from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from . import models as my_models
from .models import *

# Create your views here.


def home_page(request):
    return render(request, 'vm_home_page.html')

class search_results(ListView):
    model = Performers
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        table = getattr(my_models, self.request.GET.get('table'))
        if hasattr(table, 'name'):
            object_list = table.objects.filter(Q(name__icontains=query))
        else:
            object_list = table.objects.filter(Q(id__icontains=query))

        for item in object_list:
            print(item)


        return object_list
