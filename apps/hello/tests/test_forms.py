from hello.models import Person, Request, RequestHandler
from hello.forms import EditPersonForm
from django.test import TestCase

class EditPersonFormTest(TestCase):
    def test_initiate_basic_form(self):
        # Setup test
        data  = {
            'first_name':'Ibrahem',
            'sur_name':'Amer',
            'birth_date':'1995-5-5',
            'bio':'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            'contacts':"email: sdasd /nskype: ebrahem3amer",
            'photo': 'N/A',
        }

        # Exercise test
        form = EditPersonForm(data = data)

        # Assert test
        self.assertTrue(form.is_valid())

    def test_edit_fname_with_numbers(self):
        # Setup test
        data  = {
            'first_name':'123456',
            'sur_name':'Amer',
            'birth_date':'1995-5-5',
            'bio':'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            'contacts':"email: sdasd /nskype: ebrahem3amer",
            'photo': 'N/A',
        }
        

        # Exercise test
        form = EditPersonForm(data = data)

        # Assert test
        self.assertFalse(form.is_valid())

    def test_edit_sname_with_numbers(self):
        # Setup test
        data  = {
            'first_name':'Ibrahem',
            'sur_name':'134568',
            'birth_date':'1995-5-5',
            'bio':'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            'contacts':"email: sdasd /nskype: ebrahem3amer",
            'photo': 'N/A',
        }
        

        # Exercise test
        form = EditPersonForm(data = data)

        # Assert test
        self.assertFalse(form.is_valid())

    def test_edit_birth_date_with_date_less_than_10_years_ago(self):
        # Setup test
        data  = {
            'first_name':'Ibrahem',
            'sur_name':'Amer',
            'birth_date':'17-12-2010',
            'bio':'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            'contacts':"email: sdasd /nskype: ebrahem3amer",
            'photo': 'N/A',
        }
        

        # Exercise test
        form = EditPersonForm(data = data)

        # Assert test
        self.assertFalse(form.is_valid())

    def test_edit_image_with_valid_one(self):
        # Setup test
        data  = {
            'first_name':'Ibrahem',
            'sur_name':'Amer',
            'birth_date':'17-12-2010',
            'bio':'Relentless programmer, ambitious enterpreneur, and avid reader who traces the roots of everything.',
            'contacts':"email: sdasd /nskype: ebrahem3amer",
            'photo': 'test.jpg',
        }
        

        # Exercise test
        form = EditPersonForm(data = data)

        # Assert test
        self.assertFalse(form.is_valid())



