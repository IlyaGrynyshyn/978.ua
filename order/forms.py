from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control vRequired vChars save_data'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control vRequired vChars save_data'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control vRequired vChars save_data'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control vRequired vChars save_data'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control vRequired vChars save_data'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control vRequired vChars save_data'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'b-order-my-comment'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "Ім'я"
        self.fields['first_name'].empty_label = "Обов'язкове для заповнення"
        self.fields['last_name'].label = 'Прізвище'
        self.fields['email'].label = "E-mail"
        self.fields['email'].empty_label = "Обов'язкове для заповнення"
        self.fields['address'].label = 'Адреса'
        self.fields['address'].empty_label = "Обов'язкове для заповнення"
        self.fields['postal_code'].label = 'Коштовий код'
        self.fields['city'].label = 'Місто'
        self.fields['comment'].label = 'Кометарій'

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'comment']
