from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
   # return HttpResponse("this is aboutpage")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is servicespage")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
            
        contact = Contact(name=name, email=email, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')
   # return HttpResponse("this is contactpage")