from django.shortcuts import render, get_object_or_404
from .models import Trail, Park


def trail_catalog(request):
    trails = Trail.objects.filter(is_open=True).order_by('distance_km')
    return render(request, "catalog.html", {"trails": trails})


def trails_by_park(request, park_id):
    park = get_object_or_404(Park, pk=park_id)
    trails = Trail.objects.filter(park=park, is_open=True).order_by('distance_km')
    return render(request, "catalog.html", {"trails": trails, "park": park})
