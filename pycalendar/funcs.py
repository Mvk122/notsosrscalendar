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
        self.category_title = event.category.get_category_title_text(language)
        self.title_text = event.get_event_title_text(language)
        self.get_event_markdown = event.get_event_markdown_text(language)

        
        
