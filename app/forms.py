from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

from .models.my_user_admin import MyUserAdmin



class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme password', widget=forms.PasswordInput)

    class Meta:
        model = MyUserAdmin
        fields = ('first_name', 'last_name', 'dt_expiracao')
        labels = {'username': 'UserName/E-mail'}

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords não são iguais. ")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class UserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        fields = ('email', 'password', 'dt_expiracao', 'is_active', 'is_admin')