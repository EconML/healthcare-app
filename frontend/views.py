from django.shortcuts import render

def app(request):
    return render(request, 'frontend/base.html')
