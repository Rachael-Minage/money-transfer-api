from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.create_account, name='create_account'),
    path('accounts/<int:id>/', views.get_account, name='get_account'),
]
