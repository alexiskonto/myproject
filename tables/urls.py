from django.urls import path
from .views import dashboard, add_entry

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add/', add_entry, name='add_entry'),
]
