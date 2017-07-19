import json
from django.shortcuts import render, get_object_or_404
from hello.models import Person


def homepage_visitor(request):
    """Accepts http request, return homepage for non-authorized user."""

    person = get_object_or_404(Person, pk=1)
    person_contacts = person.contacts.replace('u', '')
    person.contacts = json.loads(person_contacts.replace("'", '"'))

    return render(request, 'home.html', {'person': person})


def latest_requests(request):
    """calls latest 10 requests in db, display template to user."""

    # Display template to user.
    return render(request, 'requests.html')
