from django.db import models

class Language(models.Model):
    short_code = models.CharField(max_length=10)
    language = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.short_code} {self.language}"

#English name should never be used, it is just for backend ease of use
#CategoryTitle of the appropriate language should be used instead
class Category(models.Model):
    english_name = models.CharField(max_length=255)
    hex_color = models.CharField(max_length=6)

    def __str__(self):
        return self.english_name

class CategoryTitle(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Event(models.Model):
    article = models.URLField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    english_title = models.TextField()
    english_description_markdown = models.TextField()

#Multiple titles per event to support multiple languages
class Title(models.Model):
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    title = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

#Multiple descriptions per event to support multiple languages
class DescriptionMarkdown(models.Model):
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    description_markdown = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)