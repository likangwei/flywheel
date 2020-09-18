from django.contrib import admin

from .models import Copy
from .models import WheelPart
from .models import Situation
from .models import Case
from .models import Weakness
from .models import Goal


def copy_offline(modeladmin, request, queryset):
    # 如果下游没有任务依赖此任务，则可以下线
    any_depend = False
    for copy in queryset.all():
        copy.depend = '下游: '
        for down in copy.downstreams.all():
            if down.id != copy.id:
                any_depend = True
            copy.depend += '%s_%s\n' % (down.id, down.name)
        if not any_depend:
            copy.status = Copy.STATUS_OFF
        copy.save()


copy_offline.short_description = "下线"


class CopyAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'depend']
    list_filter = ['status']
    actions = [copy_offline]

    class Meta:
        fields = ['name']


class SituationAdmin(admin.ModelAdmin):
    list_display = ['situation', 'principle', 'sys_level']


class CaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'principle', 'copy']
    list_filter = ['can_copy']


admin.site.register(Copy, CopyAdmin)
# admin.site.register(WheelPart)
admin.site.register(Weakness)
admin.site.register(Goal)
admin.site.register(Case, CaseAdmin)
admin.site.register(Situation, SituationAdmin)
