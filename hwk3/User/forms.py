from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(required =True)
   # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ('username','password1','password2')

    def clean_user_name(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User,DoesNotExist:
            return user_name
        raise forms.ValidationError('duplicate username')

class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)

    def is_valid(self):
        username = self.fields.get('username')
        pwd = self.fields.get('password')
        if (username is not None) and (pwd is not None):
            return True
        else:
            return False
   # username = forms.CharField(required=True#)
  #  password = forms.CharField(widget=forms.PasswordInput) 

    class Meta:
        model=User
        fields = ("username", "password")


class MessageAddForm(forms.Form):
    title = forms.CharField(required=True)
    message = forms.CharField(widget = forms.Textarea)

