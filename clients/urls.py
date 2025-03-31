from django.urls import path
from .views import ClientListView, Homepage

urlpatterns = [
    path('list', ClientListView.as_view(), name='clients-list'), #
]
