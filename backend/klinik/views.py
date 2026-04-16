from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import ClientProfile
from .serializers import ClientRegisterSerializer, CustomTokenObtainPairSerializer
from .permissions import IsPsychologist

# ==========================================
# 1. KİMLİK DOĞRULAMA (LOGIN) GÖRÜNÜMÜ
# ==========================================
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# ==========================================
# 2. DANIŞAN YÖNETİMİ GÖRÜNÜMLERİ
# ==========================================

# KORUMALI: Yeni Danışan Ekleme (Sadece Psikolog)
class ClientCreateView(generics.CreateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientRegisterSerializer
    permission_classes = [IsAuthenticated, IsPsychologist] # Güvenlik Duvarı

# KORUMALI: Danışanları Listeleme (Sadece Psikolog)
class ClientListView(generics.ListAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientRegisterSerializer
    permission_classes = [IsAuthenticated, IsPsychologist] # Güvenlik Duvarı