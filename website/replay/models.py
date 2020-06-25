from django.db import models


class Replay(models.Model):
    title = models.CharField(max_length=200)
    case_detail = models.TextField()
    reason = models.TextField()
    plan = models.TextField()
