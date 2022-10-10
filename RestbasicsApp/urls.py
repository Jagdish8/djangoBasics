from django.urls import path
from .views.CRUD import postAllInValidData

urlpatterns = [
    path('postAllInValidData/',postAllInValidData),
]
