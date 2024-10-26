from django.urls import path
from users.views import userregistrationview,userloginview
urlpatterns = [

    path('userregister/', userregistrationview, name='userregiurl'),
    path('userlogin', userloginview, name='userloginurl'),
    
]
