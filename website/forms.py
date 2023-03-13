# Importing the required modules and models
from django import forms
from django.contrib.auth.models import User
from .models import Patient1
from django.contrib.auth.forms import UserCreationForm

# Defining the UserRegisterForm class to allow user registration
class UserRegisterForm(UserCreationForm):
    
    # Adding email field to the registration form
    email = forms.EmailField()

    # Meta class to specify the model and fields to use
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Defining the PatientForm1 class for creating and updating Patient1 records
class PatientForm1(forms.ModelForm):

    # Meta class to specify the model and fields to use
    class Meta:
        model = Patient1
        fields = ['full_name', 'email', 'phone', 'desc']
