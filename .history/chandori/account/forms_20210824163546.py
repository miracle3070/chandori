from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomCsUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['hp', 'name', 'student_id', 'grade', 'circles']
