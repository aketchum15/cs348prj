from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#test fucntion for home page, change name and stuff later
def home_page(request):
    return render(request, 'venue_manager_app/vm_home_page.html')

def page2test(request):
    return render(request, 'venue_manager_app/page2test.html')

