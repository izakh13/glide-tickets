from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username',)


class CustomUserPasswordChangeForm(AdminPasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)