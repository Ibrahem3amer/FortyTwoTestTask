from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from PIL import Image



class Person(models.Model):
    # Helper variables
    msg = 'Name cannot start with number, should consist of characters.'
    name_rgx = r'^[a-zA-Z][a-zA-Z0-9]*([ ]?[a-zA-Z0-9]+)+$'
    name_validator = RegexValidator(name_rgx, msg)

    first_name = models.CharField(max_length=100, validators=[name_validator])
    sur_name = models.CharField(max_length=100, validators=[name_validator])
    birth_date = models.CharField(max_length=100, default='N/A')
    photo = models.ImageField(upload_to='/'.encode('utf-8'), default='no-img.jpg')
    contacts = models.CharField(max_length=200, default='{}')
    bio = models.CharField(max_length=700, default='N/A')

    @classmethod
    def process_user_photo(cls, person_info):
        """Edits photo dimensions to 200*200, Opens, resizes and saves it."""
        size = (200, 200)
        try:
            photo_name = settings.MEDIA_ROOT+'/'+person_info.photo.name
            photo_name = photo_name.encode('utf-8')
            image = Image.open(photo_name)
            image.thumbnail(size, Image.ANTIALIAS)
            image.save(photo_name)
        except AttributeError:
            return


class Request(models.Model):
    """Represents the request instance being sent by user."""
    scheme = models.CharField(max_length=100, default='N/A')
    body = models.CharField(max_length=500, default='N/A')
    path = models.CharField(max_length=100, default='N/A')
    method = models.CharField(max_length=100, default='N/A')
    date = models.DateTimeField(auto_now_add=True)


class RequestHandler(object):
    """Contains fields and methods that handle proccessing Request instances"""
    unread_requests_counter = 0

    @classmethod
    def save_http_request(cls, request):
        """saves request to db. Return False if smth went wrong, else True."""
        if 'requests' not in request.path:
            cls.increment_unread_requests()
        http_request = Request.objects.create(
                path=request.path,
                method=request.method,
            )
        http_request.save()
        return

    @classmethod
    def get_unread_requests(cls):
        """Returns the latest number of requests that user hasn't seen yet."""
        return cls.unread_requests_counter

    @classmethod
    def increment_unread_requests(cls):
        """Updates the number of requests that user hasn't seen yet."""
        cls.unread_requests_counter += 1
        return

    @classmethod
    def zero_unread_requests(cls):
        """Called on requests page. Make unread requests = zero."""
        cls.unread_requests_counter = 0
        return
