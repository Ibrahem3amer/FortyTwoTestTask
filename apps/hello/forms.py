from django import forms
from django.core.exceptions import ValidationError
from hello.models import Person
from hello.validators import EditPersonValidator as validator


class EditPersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'

    def clean(self):
        """Assures that birthday is in reasonable period."""

        super(EditPersonForm, self).clean()
        cleaned_data = self.cleaned_data

        # Validates that birthdate is in normal range.
        bday = cleaned_data['birth_date']
        bdate_status = validator.validate_birth_date(bday)
        if bdate_status != 1:
            raise ValidationError('Please enter a valid year.')

        return cleaned_data
