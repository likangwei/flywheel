from django.contrib import admin

# Register your models here.
from .models import Replay
from .models import Tag
from .models import Cycle

admin.site.register(Tag)


class ReplayAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'principle']
    list_filter = ['tags']
    exclude = []


class CycleAdmin(admin.ModelAdmin):
    list_display = ['goal']
    exclude = []

admin.site.register(Cycle, CycleAdmin)
admin.site.register(Replay, ReplayAdmin)
