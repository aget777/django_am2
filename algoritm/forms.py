from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='title', help_text="Заголовок", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}))
    slug = forms.SlugField(max_length=255, label='slug', help_text="URL", widget=forms.TextInput(attrs={'class': 'input_area_space', 'placeholder': 'Укажите Slug'}))
    content = forms.CharField(label='content', help_text="Описание", widget=forms.Textarea(attrs={'cols': 40, 'rows':  5, 'class': 'input_area_space', 'placeholder': 'Введите описание услуги'}))
    is_published = forms.BooleanField(label='ispublished', help_text="Опубликовать", required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="caterories", help_text="Категория", empty_label="Категория не выбрана")

