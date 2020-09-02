from django.db import models


class Flywheel(models.Model):
    name = models.CharField(max_length=200)
    rate = models.CharField(max_length=200, default="")
    rate_one_year = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class WheelPart(models.Model):
    name = models.CharField(max_length=200)
    next_part = models.ForeignKey('self',
                                  on_delete=models.SET_NULL,
                                  null=True)
    wheel = models.ForeignKey(Flywheel,
                              on_delete=models.SET_NULL,
                              null=True)

    def __str__(self):
        return self.name


class Situation(models.Model):
    situation = models.CharField(max_length=300)
    principle = models.TextField(blank=True)
    sop = models.TextField(blank=True)

    def __str__(self):
        return self.situation


class Case(models.Model):
    TYPE_GOOD = 'good'
    TYPE_BAD = 'bad'

    TYPE_CHOICES = (
        (TYPE_GOOD, 'good'),
        (TYPE_BAD, 'bad')
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default=TYPE_GOOD)

    def __str__(self):
        return self.title
