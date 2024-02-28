from django.urls import path, include

from tyytiki.views import index, about, all_products, show_prod, show_category

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('products/', all_products, name='products'),
    path('prod/<int:prod_id>/', show_prod, name='prod'),
    path('category/<int:cat_id>/', show_category, name='category'),
    ]
