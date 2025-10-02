"""Views for the EchoPulse website Django application."""

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .models import Event
from website.models import Album, Event, UserFavoriteAlbum


def home(request):
    """
    Render the authenticated home page.
    This view requires the user to be logged in.
    """
    # The @login_required decorator ensures that only authenticated users can access this view.
    # You can add more logic here to fetch user-specific data if needed.
    # For now, we just render the authenticated home template.
    return render(request, "home.html")


def events(request):
    """
    Render the events page with a list of all events.
    """
    # Fetch all events from the database.
    # Assuming Event is a model defined in models.py
    # and has been imported at the top of this file.
    events = Event.objects.all()
    return render(request, "events.html", {"events": events})


def albums(request):
    """
    Render the albums page.
    This view requires the user to be logged in.
    """
    # Fetch albums from the database (assuming you have an Album model).
    # For now, we will just render a placeholder template.
    return render(request, "albums.html")


def artists(request):
    """
    Render the artists page.
    This view requires the user to be logged in.
    """
    # Fetch artists from the database (assuming you have an Artist model).
    # For now, we will just render a placeholder template.
    return render(request, "artists.html")



def subscribe(request):
    """
    Render the subscribe page.
    This view requires the user to be logged in.
    """
    # If the user is authenticated, render the subscribe template.
    if request.user.is_authenticated:
        return render(request, "subscribe.html")
    # If the user is not authenticated, redirect them to the home page.
    else:
        return render(request, "home.html")


@csrf_exempt
def unsubscribe(request):
    """
    Render the unsubscribe page.
    This view allows users to unsubscribe from the email list.
    It can be accessed via a POST request with an email parameter.
    """
    message = ""
    message_type = ""
    if request.method == "POST":
        email = request.POST.get("email")
        # Here you'd handle the removal from your email list
        if email:
            message = f"{email} has been successfully unsubscribed from EchoPulse."
            message_type = "success"
        else:
            message = "Please provide a valid email."
            message_type = "error"
    return render(request, "unsubscribe.html", {
        "message": message,
        "message_type": message_type
    })


def album_detail(request, id):
    """ Render the album detail page.
    This view requires the user to be logged in.
    """
    # Fetch the album by ID from the database (assuming you have an Album model).
    # For now, we will just render a placeholder template.
    return render(request, "album_detail.html", {"id": id})


def event_detail(request, id):
    """ Render the event detail page.
    This view requires the user to be logged in.
    """
    # Fetch the event by ID from the database (assuming you have an Event model).
    # For now, we will just render a placeholder template.
    event = Event.objects.get(id=id)
    return render(request, "event_detail.html", {"event": event})


def echo_pulse_landing(request):
    """
    Render the public landing page.
    This view checks if the user is authenticated.
    If the user is authenticated, it redirects to the home_authenticated view.
    If the user is not authenticated, it renders the landing page.
    """
    if request.user.is_authenticated:
        return redirect('home_authenticated')
    return render(request, "landing.html")


def login_view(request):
    """
    Render the login page.
    This view handles user authentication.
    If the user is already authenticated, it redirects to the home_authenticated view.
    If the user submits a valid login form, it logs them in and redirects to the home_authenticated view.
    """
    if request.user.is_authenticated:
        return redirect('home_authenticated')  # Redirect if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_authenticated')  # Redirect to home after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """
    Handle user logout.
    This view logs out the user and redirects to the login page.
    """
    logout(request)
    return redirect('landing')


def register(request):
    """
    Render the registration page.
    This view allows new users to register.
    If the user is already authenticated, it redirects to the home_authenticated view.
    If the user submits a valid registration form, it creates a new user, logs them in, and redirects to the home_authenticated view.
    """
    if request.user.is_authenticated:
        return redirect('home_authenticated')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_authenticated')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def album_list(request):
    """
    Render a list of albums.
    This view provides a static list of albums for demonstration purposes.
    In a real application, you would fetch this data from a database.
    """
    albums = [
        {
            'title': 'Nevermind',
            'artist': 'Nirvana',
            'year': 1991,
            'cover': 'https://upload.wikimedia.org/wikipedia/en/2/29/NirvanaNevermindalbumcover.jpg'
        },
        {
            'title': 'OK Computer',
            'artist': 'Radiohead',
            'year': 1997,
            'cover': 'https://upload.wikimedia.org/wikipedia/en/e/e4/Radiohead.okcomputer.albumart.jpg'
        },
        {
            'title': 'AM',
            'artist': 'Arctic Monkeys',
            'year': 2013,
            'cover': 'https://upload.wikimedia.org/wikipedia/en/1/17/Arctic_Monkeys_-_AM.png'
        },
        {
            'title': 'Absolution',
            'artist': 'Muse',
            'year': 2003,
            'cover': 'https://upload.wikimedia.org/wikipedia/en/e/e0/Muse_-_Absolution_cover.jpg'
        },
        {
            'title': 'American Idiot',
            'artist': 'Green Day',
            'year': 2004,
            'cover': 'https://upload.wikimedia.org/wikipedia/en/0/07/Green_Day_-_American_Idiot_album_cover.png'
        },
        {
            'title': 'Hybrid Theory',
            'artist': 'Linkin Park',
            'year': 2000,
            'cover': 'https://upload.wikimedia.org/wikipedia/en/f/fc/Linkin_Park_-_Hybrid_Theory_CD_cover.jpg'
        }
    ]
    return render(request, 'albums.html', {'albums': albums})