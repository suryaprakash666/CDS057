from django.urls import path

from ngo.views import ngologinview, ngoregistrationview

urlpatterns = [
    path('login/', ngologinview, name='ngologinurl'),
    path('register', ngoregistrationview, name='ngoregistrationurl'),
]
