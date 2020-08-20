from django.contrib import admin

from .models import Flywheel
from .models import WheelPart
from .models import Situation


class FlyWheelAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        fields = ['name']


class SituationAdmin(admin.ModelAdmin):
    list_display = ['situation', 'principle']


admin.site.register(Flywheel, FlyWheelAdmin)
admin.site.register(WheelPart)
admin.site.register(Situation, SituationAdmin)

