from django.urls import path
from doctors.views import doctorregistrationview,doctorloginview

urlpatterns = [
    path('doctorregister', doctorregistrationview, name="doctorregiurl" ),
    path('doctorlogin', doctorloginview, name="doctorloginurl" ),
]
