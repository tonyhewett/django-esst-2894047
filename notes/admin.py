from django.contrib import admin

from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
   # pass    
    list_display = ('title', 'count_likes', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
admin.site.register(models.Notes, NotesAdmin)
