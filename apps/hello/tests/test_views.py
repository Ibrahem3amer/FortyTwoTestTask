from django.core.urlresolvers import reverse
from django.test import TestCase
from hello.models import Person


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
