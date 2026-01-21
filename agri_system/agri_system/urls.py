from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
admin.site.site_header = "🌾 Agri Management System Admin"
admin.site.site_title = "Agri Admin Portal"
admin.site.index_title = "Welcome to Agri Management Dashboard"

def home(request):
    return redirect('profit')

urlpatterns = [
    path('', home),                 # 👈 FIX HERE
    path('admin/', admin.site.urls),
    path('', include('finance.urls')),
]
