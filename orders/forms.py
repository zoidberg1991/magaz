from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'address', 'city']

    phone_number = forms.CharField(initial='+7' ,label="Телефон")
