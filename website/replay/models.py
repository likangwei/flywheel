from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Replay(models.Model):
    title = models.CharField(max_length=200)
    case_detail = models.TextField(blank=True)
    reason = models.TextField(blank=True)
    plan = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    create_time = models.DateTimeField(default=None)

    def __str__(self):
        return self.title


