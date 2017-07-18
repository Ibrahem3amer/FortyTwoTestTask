from django.core.urlresolvers import reverse
from django.test import TestCase
from hello.models import Person

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
