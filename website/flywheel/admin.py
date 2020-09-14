from django.contrib import admin

from .models import Copy
from .models import WheelPart
from .models import Situation
from .models import Case
from .models import Weakness


class FlyWheelAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'rate', 'rate_one_year']
    list_filter = ['status']

    class Meta:
        fields = ['name']


class SituationAdmin(admin.ModelAdmin):
    list_display = ['situation', 'principle', 'sys_level']


class CaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'principle']
    list_filter = ['can_copy']


admin.site.register(Copy, FlyWheelAdmin)
# admin.site.register(WheelPart)
admin.site.register(Weakness)
admin.site.register(Case, CaseAdmin)
admin.site.register(Situation, SituationAdmin)

