from django.shortcuts import render

# Create your views here.

def weatherpanel(request):
    return render(request,'weatherpanel.html')