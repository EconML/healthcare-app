from django.shortcuts import render

def conditionlist(request):
    return render(request, 'frontend/condition_list.html')
