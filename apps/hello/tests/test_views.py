from django.core.urlresolvers import reverse
from django.test import TestCase
from hello.models import Person, Request, RequestHandler


class user_vists_pages(TestCase):
    """Contains cases when user visits different pages."""

    def test_user_finds_homepage(self):
        """Tests homepage loading when user hits '/'"""

        # Setup test
        Person.objects.create(pk=1)
        request = reverse('visitor_homepage')
        request = self.client.get(request)

        # Exercise test
        # Assert test
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'home.html')

    def test_user_finds_requests_view(self):
        """Tests that user can find requests page."""
        # Setup test
        request = reverse('requests')
        request = self.client.get(request)

        # Exercise test
        # Assert test
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'requests.html')


class RequestTest(TestCase):

    def test_add_new_request_through_view(self):
        """Tests that middleware saves incoming request."""

        # Setup test
        self.client.get(reverse('visitor_homepage'))

        # Exercise test
        requests_in_db = Request.objects.all().count()

        # Assert test
        self.assertTrue(requests_in_db > 0)

    def test_add_more_than_one_request(self):
        """Tests that middleware saves incoming multiple request."""

        # Setup test
        for i in range(5):
            self.client.get(reverse('visitor_homepage'))

        # Exercise test
        requests_in_db = Request.objects.all().count()

        # Assert test
        self.assertTrue(requests_in_db > 4)

    def test_unread_requests(self):
        """Tests that middleware increments unread requests."""

        # Setup test
        self.client.get(reverse('visitor_homepage'))

        # Exercise test
        requests_in_db = Request.objects.all().count()
        n = RequestHandler.get_unread_requests()

        # Assert test
        self.assertTrue(requests_in_db > 0)
        self.assertTrue(n > 0)

    def test_read_the_unread(self):
        """Tests that middleware updated unread requests."""

        # Setup test
        self.client.get(reverse('visitor_homepage'))

        # Exercise test
        n = RequestHandler.get_unread_requests()
        self.client.get(reverse('requests'))
        new_n = RequestHandler.get_unread_requests()

        # Assert test
        self.assertTrue(new_n != n)
        self.assertTrue(n > new_n)
