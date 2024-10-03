from django.shortcuts import render
from . import models
from django.views import generic

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', {'destinations' : all_destinations})

class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'
