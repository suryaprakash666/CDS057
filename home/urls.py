from django.urls import path

from home.views import homepageview


urlpatterns = [
    path('',homepageview, name="homepageurl"),
]