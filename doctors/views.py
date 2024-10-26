from django.shortcuts import render

# Create your views here.
def doctorregistrationview(request):
    return render(request, 'doctorregistration.html')

def doctorloginview(request):
    return render(request, 'doctorlogin.html')
