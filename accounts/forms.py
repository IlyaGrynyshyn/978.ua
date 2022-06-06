from django import forms
from django.forms import TextInput

from accounts.models import User
from django.contrib.auth import get_user_model


class LoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваш Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ваш пароль'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Login',

        self.fields['password'].label = 'Пароль'

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Пользователь с логином "{email} не найден в системе')
        user = User.objects.filter(email=email).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': TextInput(attrs={'placeholder': 'Ваш Email', 'type': 'text'}),
            'password': TextInput(attrs={'placeholder': 'Ваш пароль'})
        }


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ваш пароль'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторіть пароль'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефону'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Ваша пошта'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Електронна пошта'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Підтвердити пароль'
        self.fields['first_name'].label = 'Ім\'я'
        self.fields['last_name'].label = 'Призвище'
        self.fields['phone'].label = 'Номер телефону'

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Данный почтовый адрес уже зарегистрирован в системе'
            )
        return email

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Паролі не співпадають')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password', 'confirm_password']
        widgets = {
            'email': TextInput(attrs={'placeholder': 'Ваш Email', 'type': 'text'}),
            'password': TextInput(attrs={'placeholder': 'Ваш пароль'}),
            'confirm_password': TextInput(attrs={'placeholder': 'Підтвердіть пароль'}),
            'first_name': TextInput(attrs={'placeholder': 'Ваше ім\'я'}),
            'last_name': TextInput(attrs={'placeholder': 'Ваше призвище'}),
            'phone': TextInput(attrs={'placeholder': 'Номер телефону'})
        }
