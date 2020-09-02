from django.contrib import admin

from .models import Flywheel
from .models import WheelPart
from .models import Situation
from .models import Case


class FlyWheelAdmin(admin.ModelAdmin):
    list_display = ['name', 'rate', 'rate_one_year']

    class Meta:
        fields = ['name']


class SituationAdmin(admin.ModelAdmin):
    list_display = ['situation', 'principle']


admin.site.register(Flywheel, FlyWheelAdmin)
# admin.site.register(WheelPart)
admin.site.register(Case)
admin.site.register(Situation, SituationAdmin)

