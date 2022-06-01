from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
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


class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(max_length=255, label='login_auth', help_text="Email", required=True,widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
    password = forms.CharField(max_length=255, label='pas_auth', help_text="Пароль", required=True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))



class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='contact_name', help_text="Заголовок", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(max_length=255, label='contact_email',  help_text="Email", required=True,widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
    content = forms.CharField(max_length=100, label='contact_content',  help_text="Сообщение", widget=forms.Textarea(attrs={'cols': 40, 'rows':  5, 'class': 'input_area_space', 'placeholder': 'Введите сообщение'}))

    captcha = CaptchaField()


class PlanForm(forms.ModelForm, forms.MultiWidget):
    MARKET = [("0", "Ozon"), ("1", "Wildberries")]
    PROD = [("0", "Техника"), ("1", "Одежда")]


    amount = forms.CharField(max_length=15, label='plan_amount', help_text="Сумма", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите сумму'}))
    count = forms.CharField(max_length=15, label='plan_count', help_text="Количество", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите сумму'}))
    date = forms.CharField(label='plan_date', help_text="Дата", widget=forms.SelectDateWidget(years=range(2021, 2023), attrs={'class': 'form-control'}))
    marketplace = forms.ChoiceField(widget=forms.RadioSelect, choices=MARKET, help_text="Маркетплейс")
    product = forms.ChoiceField(widget=forms.RadioSelect, choices=PROD, help_text="Продукция")
    user = forms.CharField(max_length=50, label='plan_uid', required=False, widget=forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'User id', 'value': '', 'id': 'plan_uid'}))

    class Meta:
        model = Plan
        fields = ['amount', 'count', 'date', 'marketplace', 'product', 'user']


class YandexDirectForm(forms.ModelForm):
    apikey = forms.CharField(max_length=50, label='yandex_direct_api', help_text="API Yandex Direct", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите API ключ из кабинета Яндекс Директ', 'value': '', 'id': 'yandex_direct_api'}))
    email = forms.EmailField(max_length=50, label='email', help_text="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email', 'value': '', 'id': 'yandex_direct_email'}))
    user = forms.CharField(max_length=50, label='yandex_direct_uid',  required=False, widget=forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'User id', 'value': '', 'id': 'yandex_direct_uid'}))

    class Meta:
        model = YandexDirectApi
        fields = ['apikey', 'email', 'user']


class YandexMetrikaForm(forms.ModelForm):
    apikey = forms.CharField(max_length=150, label='yandex_metrika_api', help_text="API Yandex Metrika", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите API ключ из кабинета Яндекс Метрика', 'value': '', 'id': 'yandex_metrika_api'}))
    email = forms.EmailField(max_length=50, label='email', help_text="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email', 'value': '', 'id': 'yandex_metrika_email'}))
    counter = forms.CharField(max_length=50, label='metrika_counter', help_text="Номер счетчика", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер счетчика Яндекс Метрики', 'id': 'yandex_metrika_counter'}))
    user = forms.CharField(max_length=50, label='yandex_metrika_uid',  required=False, widget=forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'User id', 'value': '', 'id': 'yandex_metrika_uid'}))

    class Meta:
        model = YandexMetrikaApi
        fields = ['apikey', 'email', 'counter', 'user']


class GoogleAnalyticsForm(forms.ModelForm):
    email = forms.EmailField(max_length=50, label='email', help_text="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email', 'value': '', 'id': 'ga_email'}))
    view_id = forms.CharField(max_length=50, label='ga_view', help_text="Номер представления", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер Представления Google Analytics', 'id': 'ga_view'}))
    user = forms.CharField(max_length=50, label='ga_uid',  required=False, widget=forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'User id', 'value': '', 'id': 'ga_uid'}))

    class Meta:
        model = GoogleAnalyticsApi
        fields = ['email', 'view_id', 'user']


class OzonForm(forms.ModelForm):
    apikey = forms.CharField(max_length=50, label='ozon_api', help_text="API Key Ozon", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите API ключ из кабинета Ozon','value': '', 'id': 'ozon_api'}))
    user = forms.CharField(max_length=50, label='ozon_uid',  required=False, widget=forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'User id', 'value': '', 'id': 'ozon_uid'}))

    class Meta:
        model = OzonApi
        fields = ['apikey', 'user']

class WildberriesForm(forms.ModelForm):
    apikey = forms.CharField(max_length=50, label='wb_api', help_text="API Key Wildberries", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите API ключ из кабинета Widberries', 'value': '', 'id': 'wb_api'}))
    user = forms.CharField(max_length=50, label='wb_uid',  required=False, widget=forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'User id', 'value': '', 'id': 'wb_uid'}))

    class Meta:
        model = WildberriesApi
        fields = ['apikey', 'user']
