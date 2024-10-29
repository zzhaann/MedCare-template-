from django.contrib import admin
from .models import Article, Remedy, Surgeons, Nurses

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class SurgeonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'Lastname', 'number', 'specialization')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'Lastname', 'number', 'specialization')


class NursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'Lastname', 'number', 'shift')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'Lastname', 'number', 'shift')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Remedy)
admin.site.register(Surgeons, SurgeonsAdmin)
admin.site.register(Nurses, NursesAdmin)

