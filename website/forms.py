from django import forms
from django.contrib.auth.models import User

class ProfileEditForm(forms.ModelForm):
    """
    A form for editing the profile of a User.

    Attributes:
        username (str): The user's username.
        email (str): The user's email address.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    class Meta:
        """
        Metadata for ProfileEditForm.

        Attributes:
            model (User): The model this form edits.
            fields (list): List of fields to include in the form.
            widgets (dict): Custom widgets for rendering form fields.
        """
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
