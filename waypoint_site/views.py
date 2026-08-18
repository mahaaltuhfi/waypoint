from django.shortcuts import render


def get_all_trails():
    """Week 11 catalog data: plain dicts, per WP-503."""
    return [
        {"name": "Lake Loop", "distance": 4.2, "elevation": 120, "difficulty": "easy", "is_open": True},
        {"name": "Bear Ridge", "distance": 8.5, "elevation": 600, "difficulty": "expert", "is_open": False},
        {"name": "Sunset Trail", "distance": 3.7, "elevation": 90, "difficulty": "moderate", "is_open": True},
        {"name": "Canyon Run", "distance": 12.4, "elevation": 800, "difficulty": "hard", "is_open": True},
        {"name": "Forest Path", "distance": 2.9, "elevation": 50, "difficulty": "easy", "is_open": False},
        {"name": "High Peak", "distance": 14.1, "elevation": 1100, "difficulty": "expert", "is_open": True},
    ]


def home(request):
    return render(request, "home.html", {"greeting": "Welcome to Waypoint"})


def report(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        trail = request.POST.get("trail", "")
        note = request.POST.get("note", "")
        return render(request, "thanks.html", {"name": name})
    return render(request, "report.html")


def catalog(request):
    trails = get_all_trails()
    return render(request, "catalog.html", {"trails": trails})


def search(request):
    query = request.GET.get("q", "")
    trails = get_all_trails()
    if query:
        trails = [t for t in trails if query.lower() in t["name"].lower()]
    return render(request, "search.html", {"trails": trails, "query": query})