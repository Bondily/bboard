from django.contrib import admin
from .models import Bb, Rubric


admin.site.register(Rubric)
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric', 'kind')
    list_display_links = ('title','content')
    search_fields = ('title', 'content')
admin.site.register(Bb, BbAdmin)
# Register your models here.
