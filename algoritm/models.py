from django.db import models
from django.urls import reverse


class Boards(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Наши услуги'
        verbose_name_plural = 'Наши услуги'
        ordering = ['pk']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['pk']

class Plan(models.Model):
    user = models.CharField(max_length=100, verbose_name='UID', null=True, blank=True)
    amount = models.CharField(max_length=100, verbose_name='Сумма', null=True, blank=True)
    count = models.CharField(max_length=100, verbose_name='Количество', null=True, blank=True)
    date = models.CharField(max_length=100, verbose_name='Дата', null=True, blank=True)
    marketplace = models.CharField(max_length=100, verbose_name='Маркетплейс', null=True, blank=True)
    product = models.CharField(max_length=100, verbose_name='Тип продукта', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.marketplace

    class Meta:
        verbose_name = "План"
        verbose_name_plural = "Планы"
        ordering = ['id']

class YandexDirectApi(models.Model):
    user = models.CharField(max_length=100, verbose_name='UID', null=True, blank=True)
    email = models.CharField(max_length=100, blank=True, verbose_name='Email')
    apikey = models.CharField(max_length=100, verbose_name='API Key', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Яндекс Директ АПИ"
        verbose_name_plural = "Яндекс Директ АПИ"
        ordering = ['id']

class YandexMetrikaApi(models.Model):
    user = models.CharField(max_length=100, verbose_name='UID', null=True, blank=True)
    email = models.CharField(max_length=100, blank=True, verbose_name='Email')
    counter = models.CharField(max_length=100, verbose_name='Counter Number', null=True, blank=True)
    apikey = models.CharField(max_length=100, verbose_name='API Key', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Яндекс Метрика АПИ"
        verbose_name_plural = "Яндекс Метрика АПИ"
        ordering = ['id']

class GoogleAnalyticsApi(models.Model):
    user = models.CharField(max_length=100, verbose_name='UID', null=True, blank=True)
    email = models.CharField(max_length=100, blank=True, verbose_name='Email')
    view_id = models.CharField(max_length=100, verbose_name='Counter Number', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Google Analytics АПИ"
        verbose_name_plural = "Google Analytics АПИ"
        ordering = ['id']


class OzonApi(models.Model):
    user = models.CharField(max_length=100, verbose_name='UID', null=True, blank=True)
    apikey = models.CharField(max_length=100, verbose_name='API Key', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Ozon API"
        verbose_name_plural = "Ozon API"
        ordering = ['id']

class WildberriesApi(models.Model):
    user = models.CharField(max_length=100, verbose_name='UID', null=True, blank=True)
    apikey = models.CharField(max_length=100, verbose_name='API Key', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Wildberries API"
        verbose_name_plural = "Wildberries API"
        ordering = ['id']