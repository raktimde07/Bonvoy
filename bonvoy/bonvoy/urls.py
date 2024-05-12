
from django.contrib import admin
from django.urls import path
from core.views import index, contacts

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
