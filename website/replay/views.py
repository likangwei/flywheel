from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Cycle
from .models import Goal


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def cycle(request, id):
    cycle = Cycle.objects.get(id=id)
    goals = cycle.goal_set.all()
    gs = []
    for g in goals:
        blocks = g.roadblock_set.all()
        bs = []
        for b in blocks:
            bs.append({
                "id": b.id,
                "title": b.title
            })
        gs.append({"id": g.id, "title": g.title, "blocks": bs})
    data = {"id": cycle.id, "goals": gs}
    return JsonResponse(data)
