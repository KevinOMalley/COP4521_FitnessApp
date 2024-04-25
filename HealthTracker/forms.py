from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, UserHealthInfo, WorkoutEntry, Nutrition, Sleep
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

ACTIVITY_CHOICES = (
    ('Walk', 'Walk'),
    ('Run', 'Run'),
    ('Bike', 'Bike'),
    ('Swim', 'Swim'),
    ('Pushup', 'Pushup'),
    ('Pullup', 'Pullup'),
    ('Situp', 'Situp'),
    ('Squat', 'Squat'),
    ('Jumping Jack', 'Jumping Jack'),
    ('Shrug', 'Shrug'),
)

class RecordWorkoutForm(forms.ModelForm):
    activity_type = forms.ChoiceField(choices=ACTIVITY_CHOICES)

    class Meta:
        model = WorkoutEntry
        fields = ("activity_type", "duration", "kilometers", "rest_periods", "sets", "reps", "notes", "rating")

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

        # Get the values from the form fields
        fell_asleep_approx_hour = int(self.cleaned_data['fell_asleep_approx_hour'])
        fell_asleep_approx_minute = int(self.cleaned_data['fell_asleep_approx_minute'])
        woke_up_at_hour = int(self.cleaned_data['woke_up_at_hour'])
        woke_up_at_minute = int(self.cleaned_data['woke_up_at_minute'])
        sleep_quality = self.cleaned_data['sleep_quality']
        notes = self.cleaned_data['notes']

        # Set the instance values
        instance.fell_asleep_approx = time(fell_asleep_approx_hour, fell_asleep_approx_minute)
        instance.woke_up_at = time(woke_up_at_hour, woke_up_at_minute)
        instance.sleep_quality = sleep_quality
        instance.notes = notes

        if commit:
            instance.save()
        return instance

class RecordNutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ("food_name", "calories", "meal_type", "notes")