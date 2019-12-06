from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels
from .forms import SquirrelForm

def index(request):
<<<<<<< HEAD
=======
    context = {"sightings": Squirrels.objects.all(), "field_names": Squirrels._meta.get_fields()}
    return render(request, 'Squirrel_Sightings/index.html',context)

<<<<<<< HEAD
def all_squirrels(request):
>>>>>>> b2063779c1f4a19dc126db2bd0a489f79743795e
    squirrels = Squirrels.objects.all()
    context = {
            "squirrels": squirrels,
        }
    return render(request, 'Squirrel_Sightings/index.html',context)

=======
>>>>>>> 24cfea878f2404de42106825a0bde96780e68154
def sightings(request):
    squirrels = Squirrels.objects.all()
    context = {
            "squirrels": squirrels,
        }
    return render(request, 'Squirrel_Sightings/sightings.html', context)

def coordinates(request):
    squirrels  = Squirrels.objects.all()[:100]
    context = {
            "squirrels": squirrels,
         }
    return render(request, 'Squirrel_Sightings/map.html', context)

def edit_squirrel(request, Unique_Squirrel_Id):
    squirrel = Squirrels.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        #check the form data
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel_Sightings/edit.html',context)
    else:
        form = SquirrelForm(instance=squirrel)
    context = {
            'form':form,
        }
    return render(request, 'Squirrel_Sightings/edit.html', context)
def add_squirrel(request):
    if request.method == 'POST':
        #check the form data
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel_Sightings/list/')
    else:
        form = SquirrelForm()
    context = {
            'form':form,
        }
    return render(request, '/Squirrel_Sightings/edit.html', context)
