from .models import Category, CategoryTitle, DescriptionMarkdown, Language, Event, Title

def get_language_object(language_code: str):
    try:
        return Language.objects.get(short_code=language_code)
    except:
        try:
            return Language.objects.get(short_code='en')
        except:
            english_language = Language(short_code='en', language="English")
            english_language.save()
            return english_language


def get_category_title(category: Category, language: Language) -> str:
    try:
        return CategoryTitle.objects.get(language=language, category=category).title
    except:
        return Category.english_name

def get_event_title(event: Event, language: Language) -> str:
    try:
        return Title.objects.get(language=language, event=event).title
    except:
        return event.english_title

def get_event_markdown(event: Event, language: Language) -> str:
    try:
        return DescriptionMarkdown.objects.get(
            language=language,
            event=event
        ).description_markdown
    except:
        return event.english_description_markdown
