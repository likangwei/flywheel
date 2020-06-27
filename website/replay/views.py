from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def goal(request):
    if request.method == "PUT":
        return JsonResponse({"status": 0})
    else:
        return JsonResponse({"status": 1})