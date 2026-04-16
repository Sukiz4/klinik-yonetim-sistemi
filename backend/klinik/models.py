from django.db import models
from django.contrib.auth.models import User

# 1. KİMLİK DOĞRULAMA & PROFİL (Authentication Module) [cite: 3]
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('psychologist', 'Psychologist'), ('client', 'Client')], default='client')

# 2. DANIŞAN YÖNETİMİ (Client Management Module) [cite: 4]
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_info')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True) # Genel bilgi notları

# 3. PSİKOLOG PROFİLİ (Psychologist Profile Module) [cite: 5]
class PsychologistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='psychologist_info')
    name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=200) # Uzmanlık alanı
    experience = models.CharField(max_length=100)
    clinic_address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    about = models.TextField()

# 4. RANDEVU SİSTEMİ (Appointment Module) [cite: 6]
class AppointmentSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    client = models.ForeignKey(ClientProfile, on_delete=models.SET_NULL, null=True, blank=True)

# 5. TERAPİ SÜRECİ VE SEANS NOTLARI (Therapy & Session Notes) [cite: 7, 8]
class TherapyProcess(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Devam Ediyor')
    general_notes = models.TextField(blank=True, null=True)

class SessionNote(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = models.TextField() # Seans notu içeriği

# 6. ÖDEV / GÖREV MODÜLÜ (Task / Homework Module) [cite: 9]
class Task(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    description = models.TextField() # Ödev açıklaması
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')

# 7. PSİKOLOJİK TEST MODÜLÜ (Psychological Test Module) [cite: 10]
class Test(models.Model):
    title = models.CharField(max_length=200)

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

class TestResult(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()