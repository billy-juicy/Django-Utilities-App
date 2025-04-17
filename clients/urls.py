from django.urls import path, include
from .views import ClientListView
from .views import ClientViewSet
from .views import AddComplaintFormView
from .views import ClientAutocomplete
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', ClientViewSet, basename='client-api')

urlpatterns = [
    path('list', ClientListView.as_view(), name='clients-list'),
    path('', include(router.urls)),
    path('complaint/add', AddComplaintFormView.as_view(), name='complaints-add'),
    path('complaint/success', AddComplaintFormView.as_view(), name='complaints-success'),
    path(r'autocomplete/', ClientAutocomplete.as_view(), name='clients-autocomplete',)
]
