from django.db import models


class Cycle(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Goal(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    cycle = models.ForeignKey(Cycle, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class RoadBlock(models.Model):
    """
    发现障碍
    """
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, null=True)


class RootCase(models.Model):
    """
    分析问题
    """
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    road_block = models.ForeignKey(RoadBlock, on_delete=models.SET_NULL, null=True)


class Principle(models.Model):
    content = models.TextField(blank=True)

    def __str__(self):
        return self.content


class Solution(models.Model):
    """
    方案
    """
    content = models.TextField(blank=True)
    cycle = models.ForeignKey(Cycle, on_delete=models.SET_NULL, null=True)


class Execute(models.Model):
    """
    执行
    """
    content = models.TextField(blank=True)
    cycle = models.ForeignKey(Cycle, on_delete=models.SET_NULL, null=True)


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
    principle = models.TextField(blank=True)

    def __str__(self):
        return self.title
