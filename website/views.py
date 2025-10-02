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

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page template.
    """
    return render(request, "home.html")


def events(request):
    """
    Render the events page with a list of all events.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered events page template with event data.
    """
    events = Event.objects.all()
    return render(request, "events.html", {"events": events})


def albums(request):
    """
    Render the albums page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered albums page template.
    """
    return render(request, "albums.html")


def artists(request):
    """
    Render the artists page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered artists page template.
    """
    return render(request, "artists.html")


def subscribe(request):
    """
    Render the subscribe page for authenticated users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered subscribe page if authenticated, otherwise the home page.
    """
    if request.user.is_authenticated:
        return render(request, "subscribe.html")
    else:
        return render(request, "home.html")


@csrf_exempt
def unsubscribe(request):
    """
    Allow users to unsubscribe from the email list.

    Args:
        request (HttpRequest): The HTTP request object. Should include 'email' in POST data.

    Returns:
        HttpResponse: The rendered unsubscribe page with a message about the operation status.
    """
    message = ""
    message_type = ""
    if request.method == "POST":
        email = request.POST.get("email")
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
    """
    Render the album detail page.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the album.

    Returns:
        HttpResponse: The rendered album detail page.
    """
    return render(request, "album_detail.html", {"id": id})


def event_detail(request, id):
    """
    Render the event detail page.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the event.

    Returns:
        HttpResponse: The rendered event detail page with the specific event.
    """
    event = Event.objects.get(id=id)
    return render(request, "event_detail.html", {"event": event})


def echo_pulse_landing(request):
    """
    Render the public landing page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect or HttpResponse: Redirects authenticated users to home, others see landing page.
    """
    if request.user.is_authenticated:
        return redirect('home_authenticated')
    return render(request, "landing.html")


def login_view(request):
    """
    Handle user login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect or HttpResponse: Redirects authenticated users to home, else renders login form.
    """
    if request.user.is_authenticated:
        return redirect('home_authenticated')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_authenticated')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """
    Log out the current user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the landing page.
    """
    logout(request)
    return redirect('landing')


def register(request):
    """
    Handle user registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect or HttpResponse: Redirects authenticated users to home, else renders registration form.
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
    Render a static list of albums.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered albums page with a static list of album dictionaries.
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
