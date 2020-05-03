from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', )

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        success_url = 'accounts/profile.html'
        fields = ('first_name', 'last_name', 'image', 'bio', 'current_location',)
