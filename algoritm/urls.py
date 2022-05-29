from django.urls import path

from .views import *


urlpatterns = [
    # path('', index, name='home'),
    path('', AlgoritmHome.as_view(), name='home'),
    path('products/', AlgoritmProducts.as_view(), name='products'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', AlgoritmCategory.as_view(), name='category'),
]
