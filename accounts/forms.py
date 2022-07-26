from django import forms


class UserLoginForm(forms.Form):
    username=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Username'}))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Password'}))