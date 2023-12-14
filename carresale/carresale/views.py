# views.py
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Car
from carresale.forms import CarForm

def home(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')  # Redirect to the list view after successful submission
    else:
        form = CarForm()

    return render(request, 'add_car.html', {'form': form})