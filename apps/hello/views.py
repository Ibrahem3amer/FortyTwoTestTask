import json
from django.shortcuts import render, get_object_or_404, redirect
from django.core.management import call_command
from django.http import HttpResponse
from hello.models import Person, Request, RequestHandler
from hello.forms import EditPersonForm


def homepage_visitor(request):
    """
    Accepts http request, return homepage for non-authorized user. 
    """

    # In case you want to user fixture-based data.
    person          = get_object_or_404(Person, pk = 1)
    person_contacts = person.contacts.replace('u','')
    person.contacts = json.loads(person_contacts.replace("'",'"'))
    
    return render(request, 'home.html', {'person': person})