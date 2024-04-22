from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, UserHealthInfo, Workout, FoodEntry, Sleep


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=255)
    is_under_18 = forms.BooleanField(label="Are you under 18?", required=False)
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

class AuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget = forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ("username", "password")


class HealthInfoForm(forms.ModelForm):
    class Meta:
        model = UserHealthInfo
        fields = ('weight', 'height', 'goals')

class RecordWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ("activity_type", "duration", "kilometers", "miles", "rest_periods", "sets", "reps", "notes", "rating")

class RecordFoodForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ("food_name", "calories", "meal_type", "notes")

class RecordSleepForm(forms.ModelForm):
    class Meta:
        model = Sleep
        fields = ("fell_asleep_approx", "woke_up_at", "total_sleep_duration", "sleep_quality", "notes")