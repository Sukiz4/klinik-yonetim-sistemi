from django.contrib import admin
from .models import Profile, ClientProfile, PsychologistProfile, AppointmentSlot, TherapyProcess, SessionNote, Task, Test, Question, TestResult

admin.site.register(Profile)
admin.site.register(ClientProfile)
admin.site.register(PsychologistProfile)
admin.site.register(AppointmentSlot)
admin.site.register(TherapyProcess)
admin.site.register(SessionNote)
admin.site.register(Task)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(TestResult)