# Generated by Django 5.0.2 on 2024-04-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthTracker', '0008_alter_sleep_total_sleep_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('calories', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('brunch', 'Brunch'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')], max_length=20)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='foodentry',
            name='user',
        ),
        migrations.DeleteModel(
            name='Goals',
        ),
        migrations.DeleteModel(
            name='FoodEntry',
        ),
    ]
