from hello.models import RequestHandler


class RequestsMiddleware(object):
    """Sends every incoming request to be stored in db"""

    def process_request(self, request):
        """Calls method that updates the unread requests counter."""
        RequestHandler.save_http_request(request)

        return None
