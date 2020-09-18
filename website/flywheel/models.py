from django.db import models


class Copy(models.Model):
    STATUS_ON = 'on'
    STATUS_OFF = 'off'
    STATUS_DEV = 'dev'
    STATUS_CHOICES = (
        (STATUS_ON, STATUS_ON),
        (STATUS_DEV, STATUS_DEV),
        (STATUS_OFF, STATUS_OFF),
    )
    name = models.CharField(max_length=200)
    depend = models.TextField(help_text="基础依赖", blank=True)
    how = models.TextField(help_text='如何做，请从最坏到最好依次兜底', default='', blank=True)
    rate = models.CharField(max_length=200, default="", blank=True)
    rate_one_year = models.IntegerField(default=0, blank=True)
    status = models.CharField(max_length=200, default=STATUS_OFF, choices=STATUS_CHOICES)
    depends = models.ManyToManyField('Copy', blank=True, related_name="downstreams")

    def __str__(self):
        return '%s_%s' % (self.id, self.name)

    class Meta:
        db_table = 'flywheel_flywheel'


class WheelPart(models.Model):
    name = models.CharField(max_length=200)
    next_part = models.ForeignKey('self',
                                  on_delete=models.SET_NULL,
                                  null=True)
    wheel = models.ForeignKey(Copy,
                              on_delete=models.SET_NULL,
                              null=True)

    def __str__(self):
        return self.name


class Situation(models.Model):

    SYS_LEVEL_HIGH = 3
    SYS_LEVEL_MIDDLE = 2
    SYS_LEVEL_LOW = 1
    SYS_LEVEL_NULL = 0

    SYS_LEVEL_CHOICES = (
        (SYS_LEVEL_HIGH, "高"),
        (SYS_LEVEL_MIDDLE, "中"),
        (SYS_LEVEL_LOW, "低"),
        (SYS_LEVEL_NULL, "无")
    )
    situation = models.CharField(max_length=300)
    principle = models.TextField(blank=True)
    sop = models.TextField(blank=True)
    sys_level = models.IntegerField(choices=SYS_LEVEL_CHOICES, default=SYS_LEVEL_NULL)

    def __str__(self):
        return self.situation


class Case(models.Model):
    TYPE_GOOD = 'good'
    TYPE_BAD = 'bad'

    TYPE_CHOICES = (
        (TYPE_GOOD, '成功案例'),
        (TYPE_BAD, '失败案例')
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default=TYPE_GOOD)
    recount = models.IntegerField(default=0)
    solution_short = models.TextField(blank=True, help_text="如何灭火")
    solution_middle = models.TextField(blank=True, help_text="如何控火")
    solution_long = models.TextField(blank=True, help_text="如何防火")
    principle = models.TextField(blank=True)
    can_copy = models.BooleanField(default=False)
    copy = models.ForeignKey(Copy, help_text="copy到哪了", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Weakness(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Goal(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title