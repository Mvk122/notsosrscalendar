import datetime
import calendar

from django.shortcuts import render, redirect
from django.utils import translation
from django.utils.timezone import make_aware

from pycalendar.models import Event
from pycalendar.funcs import CalendarDate
from pycalendar.getters import get_language_object

cal = calendar.Calendar()

def index(request):
    current_date = datetime.datetime.now()
    return redirect('month', year=current_date.year, month=current_date.month, language=translation.get_language_from_request(request))

def month(request, year: int, month: int, language: str='en'):

    days = [CalendarDate(date.year, date.month, date.day) for date in cal.itermonthdates(year, month)]
    events = Event.objects.filter(start_time__gte=make_aware(days[0]), start_time__lte=make_aware(days[-1]))
    language_object = get_language_object(language)

    for day in days:
        day_events = events.filter(start_time__day=day.day, start_time__month=day.month, start_time__year=day.year)
        for event in day_events:
            day.add_event(event, language_object)

    return render(request, 'pycalendar/month.html', context={'dates': days})

