# Generated by Django 5.2.3 on 2025-06-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutexercise',
            name='exercise',
        ),
        migrations.AddField(
            model_name='workoutexercise',
            name='equipment_used',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='workoutexercise',
            name='exercise_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workoutexercise',
            name='muscle_group',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='workout',
            name='notes',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='reps',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='sets',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
    ]
