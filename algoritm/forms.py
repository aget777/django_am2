from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Boards
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'slug': forms.TextInput(attrs={'class': 'input_area_space', 'placeholder': 'Укажите Slug'}),
            'content': forms.Textarea(attrs={'cols': 40, 'rows':  5, 'class': 'input_area_space', 'placeholder': 'Введите описание услуги'}),
            'cat': forms.Select(attrs={'class': 'select__area_block'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Длина должна быть меньше 100 символов')

        return title


class RegisterUserForm(UserCreationForm):
    username = forms.EmailField(max_length=255, label='login', help_text="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
    password1 = forms.CharField(max_length=255, label='pas', help_text="Пароль", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(max_length=255, label='pas2', help_text="Подтверждение пароля", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='title', help_text="Заголовок", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}))
#     slug = forms.SlugField(max_length=255, label='slug', help_text="URL", widget=forms.TextInput(attrs={'class': 'input_area_space', 'placeholder': 'Укажите Slug'}))
#     content = forms.CharField(label='content', help_text="Описание", widget=forms.Textarea(attrs={'cols': 40, 'rows':  5, 'class': 'input_area_space', 'placeholder': 'Введите описание услуги'}))
#     is_published = forms.BooleanField(label='ispublished', help_text="Опубликовать", required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="caterories", help_text="Категория", empty_label="Категория не выбрана")

