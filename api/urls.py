from django.urls import path
from api.views import ShortenURL, RedirectURLView, ListShortURL

urlpatterns = [
    path('',ShortenURL.as_view(),name='create_short_url'),
    path('<str:short_code>', RedirectURLView.as_view(), name='get_original_url'),
    path('list/', ListShortURL.as_view(), name='list_urls')


]
