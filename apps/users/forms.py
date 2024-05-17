from django import forms
from django.contrib.auth.forms import SetPasswordForm

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Новый пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Введите новый пароль", "class": "form-control"}),
    )
    new_password2 = forms.CharField(
        label="Подтвердите новый пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Подтвердите новый пароль", "class": "form-control"}),
    )
