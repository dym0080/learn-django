from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # 由于内置的UserCreationForm没有email字段，所以新建了这个类进行扩展
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
      
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')