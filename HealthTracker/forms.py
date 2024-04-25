from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, UserHealthInfo, WorkoutEntry, Nutrition, Sleep
from datetime import time, timedelta
from . import calculate

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
    weight = forms.DecimalField(disabled=True)  # Add a disabled weight field

    class Meta:
        model = WorkoutEntry
        fields = ("activity_type", "duration", "kilometers", "miles", "rest_periods", "sets", "reps", "notes", "rating")

    def init(self, user, args, **kwargs):
        super().init(args, **kwargs)
        user_health = UserHealthInfo.objects.get(user=user)  # Retrieve user's health info
        self.fields['weight'].initial = user_health.weight  # Set the initial value for the weight field

    def save(self, commit=True):
        instance = super().save(commit=False)
        mile = self.cleaned_data['miles']
        kilometer = self.cleaned_data['kilometers']
        weight = self.cleaned_data['weight_kg']
        sets = self.cleaned_data['sets']
        reps = self.cleaned_data['reps']

        if self.cleaned_data['activity_type'] == 'Walk' and self.cleaned_data['miles'] != None:
            kms = calculate.miles_to_km(mile)
            cals_burned = calculate.distance_walked_to_calories(kms, weight)
        if self.cleaned_data['activity_type'] == 'Run' and self.cleaned_data['miles'] != None:
            kms = calculate.miles_to_km(mile)
            cals_burned = calculate.distance_ran_to_calories(kms, weight)
        if self.cleaned_data['activity_type'] == 'Swam' and self.cleaned_data['miles'] != None:
            kms = calculate.miles_to_km(mile)
            cals_burned = calculate.distance_swam_to_calories(kms, weight)
        if self.cleaned_data['activity_type'] == 'Biked' and self.cleaned_data['miles'] != None:
            kms = calculate.miles_to_km(mile)
            cals_burned = calculate.distance_biked_to_calories(kms, weight)
        if self.cleaned_data['activity_type'] == 'Walk' and self.cleaned_data['kilometers'] != None:
            cals_burned = calculate.distance_walked_to_calories(kilometer, weight)
        if self.cleaned_data['activity_type'] == 'Run' and self.cleaned_data['kilometers'] != None:
            cals_burned = calculate.distance_ran_to_calories(kilometer, weight)
        if self.cleaned_data['activity_type'] == 'Swam' and self.cleaned_data['kilometers'] != None:
            cals_burned = calculate.distance_swam_to_calories(kilometer, weight)
        if self.cleaned_data['activity_type'] == 'Biked' and self.cleaned_data['kilometers'] != None:
            cals_burned = calculate.distance_biked_to_calories(kilometer, weight)

        if self.cleaned_data['activity_type'] == 'Pushup':
            cals_burned = calculate.pushup_to_calories(reps, sets, weight)
        if self.cleaned_data['activity_type'] == 'Pullup':
            cals_burned = calculate.pullup_to_calories(reps, sets, weight)
        if self.cleaned_data['activity_type'] == 'Situp':
            cals_burned = calculate.situp_to_calories(reps, sets, weight)
        if self.cleaned_data['activity_type'] == 'Squat':
            cals_burned = calculate.squat_to_calories(reps, sets, weight)
        if self.cleaned_data['activity_type'] == 'Jumping Jack':
            cals_burned = calculate.jumpingjack_to_calories(reps, sets, weight)
        if self.cleaned_data['activity_type'] == 'Shrug':
            cals_burned = calculate.shrug_to_calories(reps, sets, weight)


        instance.calories_burned = int(cals_burned)
        if commit:
            instance.save()
        return instance

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

        sleep_hour, sleep_min = calculate.sleep_calc(fell_asleep_approx_hour, fell_asleep_approx_minute, woke_up_at_hour, woke_up_at_minute)

        # Set the instance values
        instance.fell_asleep_approx = time(fell_asleep_approx_hour, fell_asleep_approx_minute)
        instance.woke_up_at = time(woke_up_at_hour, woke_up_at_minute)
        instance.total_sleep_duration = timedelta(hours=sleep_hour, minutes=sleep_min)
        instance.sleep_quality = sleep_quality
        instance.notes = notes

        if commit:
            instance.save()
        return instance

class RecordNutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ("food_name", "calories", "meal_type", "notes")