from django.shortcuts import render

# Create your views here.
def ngoregistrationview(request):
    return render(request, 'ngo_registration.html')

def ngologinview(request):
    return render(request, 'login.html')
