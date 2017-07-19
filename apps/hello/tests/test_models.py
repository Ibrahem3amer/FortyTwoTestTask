from hello.models import Person, Request
from django.test import TestCase


class PersonTest(TestCase):

    def test_add_new_person(self):
        """Tries to add new instance with correct data."""

        # Setup test
        data = {
            'f_name': 'ibrahem',
            's_name': 'amer',
            'bio': 'bla bla bla',
            'b_date': '1995-17-12',
            'contact': {
                'email': 'test_@test.com',
                'phone': '01092053058',
                'fb': 'ibrahem3amer',
                }
        }
        new_person = Person.objects.create()

        # Exercise test
        new_person.first_name = data['f_name']
        new_person.sur_name = data['s_name']
        new_person.bio = data['bio']
        new_person.birth_date = data['b_date']
        new_person.contacts = data['contact']
        new_person.save()
        db_result = Person.objects.first()

        # Assert test
        self.assertEqual(data['f_name'], db_result.first_name)
        self.assertEqual(db_result, new_person)

    def test_change_user_image_with_valid_one(self):
        """Changes ust image with another vaild one."""

        # Setup test
        data = {
            'f_name': 'ibrahem',
            's_name': 'amer',
            'bio': 'bla bla bla',
            'b_date': '1995-17-12',
            'contact': {
                'email': 'test_@test.com',
                'phone': '01092053058',
                'fb': 'ibrahem3amer',
                }
        }
        new_person = Person.objects.create()
        new_person.first_name = data['f_name']
        new_person.sur_name = data['s_name']
        new_person.bio = data['bio']
        new_person.birth_date = data['b_date']
        new_person.contacts = data['contact']
        new_person.save()
        db_result = Person.objects.first()

        # Exercise test
        db_result.photo = 'test.jpg'
        db_result.save()

        # Assert test
        self.assertIn('test.jpg', db_result.photo.path)


class RequestTest(TestCase):

    def test_create_new_request(self):
        """Creates new test with vaild data."""

        # Setup test
        data = {
            'scheme': 'http',
            'body': 'this is body',
            'path': 'request path',
            'method': 'GET',
            'date': '19-7-2017'
        }
        Request.objects.create(
            scheme=data['scheme'],
            body=data['body'],
            path=data['path'],
            method=data['method'],
            date=data['date']
        )

        # Exercise test
        requests_in_db = Request.objects.all().count()

        # Assert test
        self.assertTrue(requests_in_db > 0)

    def test_create_new_request_with_empty_fields(self):
        """Tests that default data is being added."""

        # Setup test
        Request.objects.create()

        # Exercise test
        requests_in_db = Request.objects.all().count()
        request = Request.objects.first()

        # Assert test
        self.assertTrue(requests_in_db > 0)
        self.assertEqual('N/A', request.scheme)
