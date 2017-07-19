import json
from django.shortcuts import render, get_object_or_404
from hello.models import Person, Request, RequestHandler


def homepage_visitor(request):
    """Accepts http request, return homepage for non-authorized user."""

    person = get_object_or_404(Person, pk=1)
    person_contacts = person.contacts.replace('u', '')
    person.contacts = json.loads(person_contacts.replace("'", '"'))

    return render(request, 'home.html', {'person': person})


def latest_requests(request):
    """calls latest 10 requests in db, display template to user."""

    # Checks for new unread requests.
    unread_requests = RequestHandler.get_unread_requests()

    # Calls latest 10 requests in db.
    latest_ten_reqeusts = Request.objects.order_by('-date')[:10]
    RequestHandler.zero_unread_requests()

    # Display template to user.
    return render(
        request,
        'requests.html', {
            'n': unread_requests,
            'requests': latest_ten_reqeusts
            }
    )
