from django import forms
from hello.models import Person


class EditPersonForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'personal_info'})
        )
    sur_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'personal_info'})
        )
    birth_date = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'personal_info datepicker'})
        )
    photo = forms.ImageField(
        widget=forms.FileInput(attrs={'onchange': 'handleFiles(this.files)'}),
        required=False
        )
    contacts = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'personal contact_area'})
        )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'personal_info bio_area'})
        )

    class Meta:
        model = Person
        fields = '__all__'
