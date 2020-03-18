from django.shortcuts import render
from django.views.generic import ListView

from .models import Condition

# Create your views here.
class ConditionListView(ListView):
    model = Condition
    template_name = 'condition_list.html'
