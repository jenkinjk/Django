from django.db import models
from django.core.validators import RegexValidator

class contact(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  phone_number = models.CharField(validators=[phone_regex], blank=True, max_length = 15)
  email_address = models.EmailField(max_length = 100)
  street_regex = RegexValidator(regex=r'd{1,4} [a-zA-Z ]*', message="Street addresses must be entered as a one to four digit number, followed by the street name (Which should contain only letters).")
  street_address = models.CharField(max_length = 100)
  def __str__(self):
    return self.first_name+" "+self.last_name
  
  def getFullName(self):
    return self.first_name+" "+self.last_name
