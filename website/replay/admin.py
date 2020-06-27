from django.contrib import admin

# Register your models here.
from .models import Replay
from .models import Tag
from .models import Cycle

admin.site.register(Tag)
admin.site.register(Cycle)


class ReplayAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'principle']
    list_filter = ['tags']
    exclude = []


class CycleAdmin(admin.ModelAdmin):
    list_display = ['']

admin.site.register(Replay, ReplayAdmin)
