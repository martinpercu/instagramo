""" Django Forms for users """

# Django
from django import forms
from django.core.exceptions import ValidationError

# Models
from django.contrib.auth.models import User
from users.models import Profile



class SignupForm(forms.Form):
    """ Sirg up form """

    username = forms.CharField(min_length=4, max_length=48)
    
    password = forms.CharField(
        max_length=72, 
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=72, 
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=48)
    last_name = forms.CharField(min_length=2, max_length=48)

    email = forms.CharField(
        min_length=6,
        max_length=90,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """ username must to be unique """
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise ValidationError("User name is already used for another one")
        return username

    def clean(self):
        """ Verify password and passwords confirmation MATCH"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise ValidationError('Passwords are not the same!')

        return data
    
    def save(self):
        """ Create user and Profile --- Is both at same time """
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """ Profile form """

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=14, required=False)
    picture = forms.ImageField()

