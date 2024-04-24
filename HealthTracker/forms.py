from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, UserHealthInfo, Workout, Nutrition, Sleep
from datetime import time, datetime, timedelta

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
        model =  Nutrition
        fields = ("food_name", "calories", "meal_type", "notes")

# class RecordSleepForm(forms.ModelForm):
#     class Meta:
#         model = Sleep
#         fields = ("fell_asleep_approx", "woke_up_at", "sleep_quality", "notes")

class RecordSleepForm(forms.ModelForm):
    HOURS = [(str(i), '{:02d}'.format(i)) for i in range(24)]
    MINUTES = [(str(i), '{:02d}'.format(i)) for i in range(60)]

    fell_asleep_approx_hour = forms.ChoiceField(choices=HOURS)
    fell_asleep_approx_minute = forms.ChoiceField(choices=MINUTES)
    woke_up_at_hour = forms.ChoiceField(choices=HOURS)
    woke_up_at_minute = forms.ChoiceField(choices=MINUTES)

    class Meta:
        model = Sleep
        fields = (
        "fell_asleep_approx_hour", "fell_asleep_approx_minute", "woke_up_at_hour", "woke_up_at_minute", "sleep_quality",
        "notes")

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Set all values to some default values for testing
        instance.fell_asleep_approx = time(22, 0)  # 10 PM
        instance.woke_up_at = time(6, 0)  # 6 AM
        instance.total_sleep_duration = timedelta(hours=8)  # 8 hours
        instance.sleep_quality = 'rested'
        instance.notes = 'Test note'

        if commit:
            instance.save()
        return instance