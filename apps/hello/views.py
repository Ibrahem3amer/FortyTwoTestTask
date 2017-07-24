import json
from collections import OrderedDict
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from hello.models import Person, Request, RequestHandler
from hello.forms import EditPersonForm


def homepage_visitor(request):
    """Accepts http request, return homepage for non-authorized user."""

    person = get_object_or_404(Person, pk=1)
    person_contacts = person.contacts.replace('u', '')
    OrderedDict([('email', 1), ('jabber', 2), ('skype', 3)]) 
    person.contacts = json.loads(person_contacts.replace("'", '"'), object_pairs_hook=OrderedDict)


    return render(request, 'home.html', {'person': person, 'request': request})


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


@login_required()
def edit_info(request):
    """
    GET request -> displays fillable form to user.
    POST request -> processes form, redirects user to homepage.
    """
    person = Person.objects.first()
    form = EditPersonForm(
        request.POST or None,
        request.FILES or None,
        instance=person
    )
    if request.method == 'POST':
        if(form.is_valid()):
            person_info = form.save()
            # Process user photo.
            if request.FILES:
                Person.process_user_photo(person_info)
            response = {}
            response['result'] = 'success'
            response['user_name'] = person_info.first_name+person_info.sur_name

            return HttpResponse(
                json.dumps(response),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({'status': 'failure. cannot save form.'}),
                content_type="application/json"
            )

    return render(request, 'edit_data.html', {'form': form})
