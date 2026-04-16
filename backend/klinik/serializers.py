from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ClientProfile, Profile

class ClientRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ClientProfile
        fields = ['username', 'password', 'full_name', 'phone', 'email', 'notes']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        # 1. Önce User tablosuna kayıt atıyoruz (Şifreyi kriptografik olarak hashler)
        user = User.objects.create_user(username=username, password=password)

        # 2. Profile tablosuna 'client' rolü ile bağlıyoruz
        Profile.objects.create(user=user, role='client')

        # 3. Kalan bilgilerle ClientProfile (Danışan) kaydını oluşturuyoruz
        client_profile = ClientProfile.objects.create(user=user, **validated_data)

        return client_profile
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Varsayılan token'ı alıyoruz
        token = super().get_token(user)

        # İçine kendi özel verilerimizi (claim) ekliyoruz
        # Kullanıcının bir profili varsa rolünü al, yoksa 'unknown' ata
        if hasattr(user, 'profile'):
            token['role'] = user.profile.role
        else:
            token['role'] = 'unknown'
            
        token['username'] = user.username
        
        return token