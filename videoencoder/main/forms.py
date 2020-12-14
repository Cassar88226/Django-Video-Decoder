from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': "id_username"}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'id': "id_username"}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': "id_password"}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': "id_password"}), required=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'password1','password2')
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
