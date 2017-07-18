from test_assignment.models import RequestHandler

class RequestsMiddleware(object):
    """Middleware that send every incoming httprequest to custom method to store this request in db"""


    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        """
        Accepts the request, call model method that takes the request as parameter. Updates the unread requests counter. 
        """
        RequestHandler.save_http_request(request)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
