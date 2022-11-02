from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from .models import Performers

# Create your views here.

#test fucntion for home page, change name and stuff later
def home_page(request):
    return render(request, 'venue_manager_app/vm_home_page.html')

class search_results(ListView):
    model = Performers
    template_name = 'search.html'

    def get_results(self):
        query = self.request.GET.get("search")
        object_list = Performers.objects.filter(Q(name__icontains=query))
        return  object_list

