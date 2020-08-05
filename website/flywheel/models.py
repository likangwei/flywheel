from django.db import models


class Flywheel(models.Model):
    name = models.CharField(max_length=200)

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