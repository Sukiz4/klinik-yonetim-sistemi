from rest_framework import permissions

class IsPsychologist(permissions.BasePermission):
    """
    Sadece rolü 'psychologist' olan kullanıcıların erişimine izin verir.
    """
    def has_permission(self, request, view):
        # 1. Kullanıcı giriş yapmış mı?
        # 2. Profili var mı?
        # 3. Rolü psikolog mu?
        return bool(
            request.user and 
            request.user.is_authenticated and 
            hasattr(request.user, 'profile') and 
            request.user.profile.role == 'psychologist'
        )