from django import forms
from .models import CamDB
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
        }
        help_texts = {
            'username': None,
            'password1': 'Введите пароль',
            'password2': 'Повторите пароль для подтверждения',
        }
    
    def clean_password1(self):
        cd = self.cleaned_data
        if len(cd['password1']) < 6:
            raise forms.ValidationError('Пароль должен быть не менее 6 символов.')
        return cd['password1']

class CamDBForm(forms.ModelForm):
    class Meta:
        model = CamDB
        fields = ['title', 'author', 'views', 'position']
        labels = {
            'title': 'Название',
            'author': 'Автор',
            'views': 'Просмотры',
            'position': 'Позиция',
        }
        help_texts = {
            'title': 'Введите название объявления.',
            'author': 'Введите имя автора.',
            'views': 'Введите количество просмотров.',
            'position': 'Введите позицию объявления.',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название объявления'}),
            'author': forms.TextInput(attrs={'placeholder': 'Автор'}),
            'views': forms.NumberInput(attrs={'placeholder': 'Просмотры'}),
            'position': forms.NumberInput(attrs={'placeholder': 'Позиция'}),
        }
