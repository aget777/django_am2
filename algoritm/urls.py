from django.urls import path

from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', cache_page(60)(AlgoritmHome.as_view()), name='home'),
    path('', AlgoritmHome.as_view(), name='home'),
    # path('', index, name='home'),
    path('', AlgoritmHome.as_view(), name='home'),
    # path('products/', cache_page(60)(AlgoritmProducts.as_view()), name='products'),
    path('products/', AlgoritmProducts.as_view(), name='products'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUsers.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', AlgoritmCategory.as_view(), name='category'),
    path('formspage/', FormsPage.as_view(), name='formspage'),
    path('page-plan-form/', AddPlan.as_view(), name='page_plan_form'),
    path('api-yandex-direct-form/', AddYandexDirectApiKey.as_view(), name='api_yandex_direct_form'),
    path('api-yandex-metrika-form/', AddYandexMetrikaApiKey.as_view(), name='api_yandex_metrika_form'),
    path('api-google-analytics-form/', AddGoogleAnalyticsApiKey.as_view(), name='api_google_analytics_form'),
    path('ozon-api-form/', AddOzonApiKey.as_view(), name='ozon_api_form'),
    path('api-wildberries-form/', AddWildberriesApiKey.as_view(), name='api_wildberries_form'),
]
