from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import StoreUser


class StoreUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = StoreUser
        fields = ('phone', 'first_name', 'last_name', 'address', 'is_active', 'is_staff', 'is_superuser')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if self.instance.pk:
            if StoreUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Phone already exists.')
        else:
            if StoreUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('Phone already exists.')

        if not phone.isdigit():
            raise forms.ValidationError('phone must be a number.')

        if not phone.startswith('09'):
            raise forms.ValidationError('phone must start with 09 digits.')

        if len(phone) != 11:
            raise forms.ValidationError('phone must have 11 digits.')

        return phone


class StoreUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = StoreUser
        fields = ('phone', 'first_name', 'last_name', 'address', 'is_active', 'is_staff', 'is_superuser')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if self.instance.pk:
            if StoreUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Phone already exists.')
        else:
            if StoreUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('Phone already exists.')

        if not phone.isdigit():
            raise forms.ValidationError('phone must be a number.')

        if not phone.startswith('09'):
            raise forms.ValidationError('phone must start with 09 digits.')

        if len(phone) != 11:
            raise forms.ValidationError('phone must have 11 digits.')

        return phone
