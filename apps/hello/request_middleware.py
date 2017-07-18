from test_assignment.models import RequestHandler


class RequestsMiddleware(object):
    """Sends every incoming request to be stored in db"""

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        """Calls method that updates the unread requests counter."""
        RequestHandler.save_http_request(request)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
