from django.shortcuts import render

# Create your views here.
def userregistrationview(request):
    return render(request, 'userregistration.html')

def userloginview(request):
    return render(request, 'userlogin.html')
