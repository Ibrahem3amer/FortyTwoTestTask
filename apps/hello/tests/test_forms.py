from hello.forms import EditPersonForm
from django.test import TestCase


class EditPersonFormTest(TestCase):

    def test_initiate_basic_form(self):
        """Tests the creation of form with basic valid data."""

        # Setup test
        data = {
            'first_name': 'Ibrahem',
            'sur_name': 'Amer',
            'birth_date': '1995-5-5',
            'bio': 'bla bal bla.',
            'contacts': "email: sdasd /nskype: ebrahem3amer",
            'photo': 'N/A',
        }

        # Exercise test
        form = EditPersonForm(data=data)

        # Assert test
        self.assertTrue(form.is_valid())

    def test_edit_fname_with_numbers(self):
        """Tests creation with invalid fname."""

        # Setup test
        data = {
            'first_name': '123456ibrahem',
            'sur_name': 'Amer',
            'birth_date': '1995-5-5',
            'bio': 'bla bal bla.',
            'contacts': "email: sdasd /nskype: ebrahem3amer",
            'photo': 'N/A',
        }

        # Exercise test
        form = EditPersonForm(data=data)

        # Assert test
        self.assertFalse(form.is_valid())

    def test_edit_sname_with_numbers(self):
        """Tests creation with invalid sname."""

        # Setup test
        data = {
            'first_name': 'Ibrahem',
            'sur_name': '1adel',
            'birth_date': '1995-5-5',
            'bio': 'bla bal bla.',
            'contacts': "email: sdasd /nskype: ebrahem3amer",
            'photo': 'N/A',
        }

        # Exercise test
        form = EditPersonForm(data=data)

        # Assert test
        self.assertFalse(form.is_valid())

    def test_edit_birth_date_with_date_less_than_10_years_ago(self):
        """Tests creation with invalid birthday."""

        # Setup test
        data = {
            'first_name': 'Ibrahem',
            'sur_name': 'Amer',
            'birth_date': '17-12-2010',
            'bio': 'Relentless programmer.',
            'contacts': "email: sdasd /nskype: ebrahem3amer",
            'photo': 'N/A',
        }

        # Exercise test
        form = EditPersonForm(data=data)

        # Assert test
        self.assertFalse(form.is_valid())
