from django.urls import path
from .views import ClientCreateView, CustomTokenObtainPairView, ClientListView

urlpatterns = [
    # DANIŞAN YÖNETİMİ
    path('api/clients/create/', ClientCreateView.as_view(), name='create-client'),
    path('api/clients/list/', ClientListView.as_view(), name='list-clients'),
    
    # KİMLİK DOĞRULAMA (LOGIN)
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]