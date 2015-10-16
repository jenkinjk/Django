from django import forms
from django.core.validators import RegexValidator

class contactForm(forms.Form):
  first_name = forms.CharField(label = 'First Name', max_length=100)
  last_name = forms.CharField(label = 'Last Name', max_length=100)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  phone_number = forms.CharField(label='Phone Number', validators=[phone_regex], max_length = 15)
  email_address = forms.EmailField(label = 'Email',max_length = 100)
  street_regex = RegexValidator(regex=r'd{1,4} [a-zA-Z ]*', message="Street addresses must be entered as a one to four digit number, followed by the street name (Which should contain only letters).")
  street_address = forms.CharField(label = 'Street Address', max_length = 100)

class loginForm(forms.Form):
  username = forms.CharField(label = 'Username:', max_length=100)
  password = forms.CharField(label = 'Password:', max_length=100)

class searchForm(forms.Form):
  search = forms.CharField(label = "Search for:", max_length=100)
