from django.shortcuts import render
from races.models import Race
from datetime import date

def main(request):
    current_date = date.today()
    next_race = Race.objects.filter(date__gte=current_date).order_by('date').first()
    return render(request, "main.html", {'next_race': next_race})