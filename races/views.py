from django.shortcuts import render , get_object_or_404
from .models import Race
from datetime import date
# Create your views here.

def race_list(request):
    corrent_date = date.today()
    races = Race.objects.all()

    next_race = races.filter(date__gte=corrent_date).order_by('date').first()
    
    return render(request, './race_list.html', {
        'races': races, 'corrent_date': corrent_date, 'next_race': next_race
        })

def race_detail(request, pk):
    race = get_object_or_404(Race, pk=pk)
    return render(request, 'race_detail.html', {'race': race})








