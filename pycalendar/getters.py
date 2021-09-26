from .models import Language

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
