from django.contrib.auth.forms import forms
from profile_app.models import ProfileAddOnModel


class ProfileAddOnForm(forms.ModelForm):
    my_bio = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'some words that defines you'}))

    class Meta:
        model = ProfileAddOnModel
        exclude = ('owner', )


class ProfileEditOnForm(forms.ModelForm):
    my_bio = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'some words that defines you'}))

    class Meta:
        model = ProfileAddOnModel
        exclude = ('owner', )
