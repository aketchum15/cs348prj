from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#test fucntion for home page, change name and stuff later
def testfunc(request):
    return render(request, 'venue_manager_app/vm_home_page.html')


