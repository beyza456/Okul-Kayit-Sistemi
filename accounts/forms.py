# Bu dosya, kullanıcıdan giriş bilgilerini almak için kullanılan Django formunu tanımlar.
# UserLoginForm, kullanıcı adı ve şifre alanlarını içerir ve giriş formunun arayüzünü özelleştirir.

from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

