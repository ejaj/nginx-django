from django.shortcuts import render
from django.views.decorators.cache import cache_control


@cache_control(private=True)
def vary(request):
    return render(request, "vary.html")
