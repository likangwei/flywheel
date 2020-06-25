from django.contrib import admin

# Register your models here.
from .models import Replay
from .models import Tag

admin.site.register(Tag)


class ReplayAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time']
    exclude = []


admin.site.register(Replay, ReplayAdmin)
