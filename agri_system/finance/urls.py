from django.urls import path
from .views import profit_loss

urlpatterns = [
    path('profit/', profit_loss, name='profit'),
]
