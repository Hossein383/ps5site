from django import forms
from . import models
from django.core.exceptions import ValidationError
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body'] 

class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری' , widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='پسورد' , widget=forms.PasswordInput(attrs={"class": "form-control"}))

class SingUpForm(forms.Form):
    username = forms.CharField(label='نام کاربری' , widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='پسورد' , widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='تکرار پسورد' , widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField()

    def clean(self):
        super().clean()

        ps1 = self.cleaned_data['password1']
        ps2 = self.cleaned_data['password2']
        if ps1 != ps2:
            raise ValidationError('پسورد ها باهمدیگه برابر نیستند.')
        