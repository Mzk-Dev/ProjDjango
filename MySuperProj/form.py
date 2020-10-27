from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import Textarea

from mysite.models import Comments, Profile


#Форма для регистрации
class SignUpForm(UserCreationForm):


    first_name = forms.CharField(max_length=30, required=False, help_text='Необязательно')
    last_name = forms.CharField(max_length=30, required=False, help_text='Необязательно')
    email = forms.EmailField(max_length=254, help_text='Введите правильный адрес электронной почты')

    class Meta:
        model = User
        fields = [ 'username' , 'first_name' , 'last_name' , 'email', 'password1' , 'password2']


#форма для входа на сайт
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#форма для  комментов
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget = Textarea(attrs={'rows':5})

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'avatar')
