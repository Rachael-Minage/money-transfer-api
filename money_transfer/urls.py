from django.urls import path
from . import views

urlpatterns = [
    path('transfers/', views.transfer_create_view, name='transfer-create'),
    
]

