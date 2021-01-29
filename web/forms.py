from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Contact


# registration form
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=40)

    # define the fields
    class Meta:
        model = User
        fields = ("first_name",
                  "last_name",
                  "username",
                  "email",
                  "password1",
                  "password2"
                  )

    # clean the email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Emailadresse wurde bereits verwendet!')
        return email

    # clean the pw
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # check if pw1 and pw2 are the same
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['Passwörter stimmen nicht überein!'],
                code='password_mismatch',
            )
        password_validation.validate_password(
            self.cleaned_data['password2'],
            self.instance
        )
        return password2

    # create new user
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        self.clean_email()
        self.clean_password()
        if commit:
            user.save()
        return user


# form for change the user name, email and username
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


# form for the contact page
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
