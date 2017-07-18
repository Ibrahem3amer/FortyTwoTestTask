from django.core.urlresolvers import resolve
from django.urls import reverse
from django.test import TestCase
from test_assignment.models import Person

class user_vists_homepage(TestCase):
    def test_user_find_homepage(self):
        # Setup test
        user    = Person.objects.create(pk = 1)
        request = reverse('visitor_homepage')
        request = self.client.get(request)

        # Exercise test

        # Assert test
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'home.html')

    def test_request_view(self):
        # Setup test
        request = reverse('request_page')
        request = self.client.get(request)

        # Exercise test
        # Assert test
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'requests.html')

class user_edits_personal_info(TestCase):
    def test_user_access_edit_page(self):
        # Setup test
        user    = Person.objects.create(pk = 1)
        request = reverse('edit_personal_data')
        request = self.client.get(request)

        # Exercise test
        # Assert test
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'edit_data.html')

    def test_user_submits_valid_post_request_and_redirected(self):
        # Setup test
        user            = Person.objects.create(pk = 1)
        request         = reverse('edit_personal_data')
        data            = {
            'first_name':'Ibrahem',
            'sur_name':'Amer',
            'birth_date':'1995-17-12',
            'bio':'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            'contacts':"email: sdasd /nskype: ebrahem3amer",
        }
        request         = self.client.post(request, data = data)

        # Exercise test
        # Assert test
        self.assertIn('success', str(request.content))
