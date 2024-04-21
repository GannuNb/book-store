from django import forms
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from .models import Order

def validate_zip_code(value):
    if not value.isdigit() or len(value) != 6:
        raise forms.ValidationError('Zip code must be a 6-digit number')

def validate_account_no(value):
    if not value.isdigit() or len(value) < 5 or len(value) > 14:
        raise forms.ValidationError('Account number must be between 5 and 14 digits long')

def validate_transaction_id(value):
    if not value.isdigit() or len(value) < 5 or len(value) > 12:
        raise forms.ValidationError('Transaction ID must be between 5 and 12 digits long')

def validate_name(value):
    if not value.isalpha():
        raise forms.ValidationError('Name must contain only alphabetic characters')

def validate_email(value):
    if not value.endswith('@gmail.com'):
        raise forms.ValidationError('Email must end with "@gmail.com"')

class OrderCreateForm(forms.ModelForm):
    DIVISION_CHOICES = (
        ('Andhra', 'Andhra'),
        ('Telangana', 'Telangana'),
        ('Banglore', 'Banglore'),
    )

    DISTRICT_CHOICES = (
        ('Kadapa', 'Anantapuram'),
        ('Nellore', 'Vijayawada'),
        ('Chitoor', 'Guntur'),
        ('Kurnool', 'Kurnool'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('Rocket', 'UPI'),
        ('Bkash', 'Cash on Delivery')
    )

    name = forms.CharField(max_length=30, required=True, validators=[validate_name])
    email = forms.EmailField(required=True, validators=[validate_email])
    phone = forms.CharField(max_length=10, required=True, validators=[RegexValidator(regex='^[0-9]{10}$', message="Phone number should be 10 digits long")])
    zip_code = forms.CharField(max_length=6, required=True, validators=[validate_zip_code])
    account_no = forms.CharField(max_length=14, required=True, validators=[validate_account_no])
    transaction_id = forms.CharField(max_length=12, required=True, validators=[validate_transaction_id])

    division = forms.ChoiceField(choices=DIVISION_CHOICES)
    district = forms.ChoiceField(choices=DISTRICT_CHOICES)
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
