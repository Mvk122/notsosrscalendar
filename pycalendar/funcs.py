import datetime

from pycalendar.models import Event, Language
from .getters import *

class CalendarDate(datetime.datetime):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.events = []

    def add_event(self, event: Event, language: Language):
        assert type(event) == Event
        self.events.append(EventDisplay(event, language))


class EventDisplay(object):
    def __init__(self, event: Event, language: Language):
        self.article = event.article
        self.start_time = event.start_time
        self.end_time = event.end_time
        self.category = event.category
        self.category_title = get_category_title(event.category, language)
        self.title_text = get_event_title(event, language)
        self.get_event_markdown = get_event_markdown(event, language)

        
        
