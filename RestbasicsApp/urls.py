from django.urls import path
from .views.CRUD import getAllInValidData

urlpatterns = [
    path('getAllInValidData/',getAllInValidData),
]
