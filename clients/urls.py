from django.urls import path
from .views import ClientListView
from .views import AddComplaintFormView
from .views import ClientAutocomplete

urlpatterns = [
    path('list', ClientListView.as_view(), name='clients-list'),
    path('complaint/add', AddComplaintFormView.as_view(), name='complaints-add'),
    path('complaint/success', AddComplaintFormView.as_view(), name='complaints-success'),
    path(r'autocomplete/', ClientAutocomplete.as_view(), name='clients-autocomplete',)
]
