from django.urls import path
from .views import ClientListView
from .views import AddComplaintFormView

urlpatterns = [
    path('list', ClientListView.as_view(), name='clients-list'),
    path('complaint/add', AddComplaintFormView.as_view(), name='complaints-add'),
    path('complaint/success', AddComplaintFormView.as_view(), name='complaints-success'),
]
