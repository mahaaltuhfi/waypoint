from django.shortcuts import render
from waypoint_site.forms import ContactForm


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
