from django.urls import path

from .views import ConditionListView

urlpatterns = [
    path('', ConditionListView.as_view(), name='home'),
]
