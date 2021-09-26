from django.contrib import admin
from pycalendar.models import * 

class TitleInline(admin.StackedInline):
    model = Title

class DescriptionMarkdownInline(admin.StackedInline):
    model = DescriptionMarkdown

class EventAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
        DescriptionMarkdownInline
    ]

class CategoryTitleInline(admin.StackedInline):
    model = CategoryTitle

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryTitleInline]
    

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Language)
