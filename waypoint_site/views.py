from django.shortcuts import render
from waypoint_site.forms import ContactForm
from waypoint_core.distance import Distance
from waypoint_core.trail import DayHike, BackpackingRoute, TrailRun


def home(request):
    return render(request, "home.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, "thanks.html", {"name": form.cleaned_data["name"]})
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def get_all_trails():
    return [
        DayHike(1, "Ridge Walk", Distance(8, "km"), 200, "moderate"),
        BackpackingRoute(2, "Coastal Trek", Distance(40, "km"), 900, "hard"),
        TrailRun(3, "Sprint Loop", Distance(5, "km"), 50, "easy"),
    ]


def catalog(request):
    trails = get_all_trails()
    return render(request, "catalog.html", {"trails": trails})


def search(request):
    query = request.GET.get("q", "")
    trails = get_all_trails()
    if query:
        trails = [t for t in trails if query.lower() in t.name.lower()]
    return render(request, "catalog.html", {"trails": trails, "query": query})
