# Waypoint

A Django web app built on top of a custom Python domain engine (Distance, Trail, Itinerary classes).

## Setup

1. Clone the repo
2. Create and activate a virtual environment:
   python -m venv env
   env\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Start the dev server:
   python manage.py runserver
6. Visit http://127.0.0.1:8000
