from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('klinik.urls')), # API yollarımızı ana sisteme bağladık
]