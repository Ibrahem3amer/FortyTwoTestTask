from hello.models import Person, Request, RequestHandler
from django.test import TestCase
from django.core.urlresolvers import reverse

class PersonTest(TestCase):
    def test_add_new_person(self):
        # Setup test
        data        = {'f_name': 'ibrahem', 's_name': 'amer', 'bio': 'bla bla bla', 'b_date': '1995-17-12', 'contact': {'email': 'test_@test.com', 'phone': '01092053058', 'fb': 'ibrahem3amer'}}
        new_person  = Person.objects.create() 

        # Exercise test
        new_person.first_name   = data['f_name']
        new_person.sur_name     = data['s_name']
        new_person.bio          = data['bio']
        new_person.birth_date   = data['b_date']
        new_person.contacts     = data['contact']
        new_person.save()
        db_result               = Person.objects.first()

        # Assert test
        self.assertEqual(data['f_name'], db_result.first_name)
        self.assertEqual(db_result, new_person)

    def test_change_user_image_with_valid_one(self):
        # Setup test
        data        = {'f_name': 'ibrahem', 's_name': 'amer', 'bio': 'bla bla bla', 'b_date': '1995-17-12', 'contact': {'email': 'test_@test.com', 'phone': '01092053058', 'fb': 'ibrahem3amer'}}
        new_person  = Person.objects.create() 
        new_person.first_name   = data['f_name']
        new_person.sur_name     = data['s_name']
        new_person.bio          = data['bio']
        new_person.birth_date   = data['b_date']
        new_person.contacts     = data['contact']
        new_person.save()
        db_result               = Person.objects.first()

        # Exercise test
        db_result.photo = 'test.jpg'
        db_result.save()


        # Assert test
        self.assertIn('test.jpg',db_result.photo.path)
