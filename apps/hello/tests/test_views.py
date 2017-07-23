from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from hello.models import Person, Request, RequestHandler


class user_vists_pages(TestCase):
    """Contains cases when user visits different pages."""

    def create_auth(self):
        """Creates auth settings for test client."""
        person = Person.objects.create(pk=1)
        membership = User.objects.create_user(
            username='admin',
            password='admin'
        )
        membership.save()
        person.membership = membership
        person.save()
        self.client.login(username='admin', password='admin')

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

    def test_user_access_edit_page_unatuh(self):
        """Tests that user can not access when unauthed."""

        # Setup test
        request = reverse('edit_personal_data')
        request = self.client.get(request)

        # Exercise test
        # Assert test
        self.assertEqual(request.status_code, 302)

    def test_user_access_edit_page_authed(self):
        """Tests that user can access edit when authed."""

        # Setup test
        self.create_auth()
        request = reverse('edit_personal_data')
        request = self.client.get(request)

        # Exercise test
        # Assert test
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'edit_data.html')

    def test_user_submits_valid_post_request(self):
        """Tests view behavior when using POST."""

        # Setup test
        self.create_auth()
        request = reverse('edit_personal_data')
        data = {
            'first_name': 'Ibrahem',
            'sur_name': 'Amer',
            'birth_date': '1995-12-17',
            'bio': 'bla bla bla.',
            'contacts': "email: sdasd /nskype: ebrahem3amer",
        }
        request = self.client.post(request, data=data)

        # Exercise test
        # Assert test
        self.assertIn('success', str(request.content))

    def test_user_submits_invalid_post_request(self):
        """Tests view behavior when using POST improbably."""

        # Setup test
        self.create_auth()
        request = reverse('edit_personal_data')
        data = {}
        request = self.client.post(request, data=data)

        # Exercise test
        # Assert test
        self.assertIn('failure', str(request.content))


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
