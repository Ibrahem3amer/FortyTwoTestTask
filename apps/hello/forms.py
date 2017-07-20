from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from hello.models import Person
from hello.validators import EditPersonValidator

class EditPersonForm(forms.ModelForm):

    class Meta:
        model       = Person
        fields      = '__all__'
    
    def clean(self):
        
        super(EditPersonForm, self).clean()
        cleaned_data = self.cleaned_data

        # Validates that birthdate is in normal range.
        bdate_status = EditPersonValidator.validate_birth_date(cleaned_data['birth_date'])
        if bdate_status != 1:
            raise ValidationError('Please enter a valid year.')

        