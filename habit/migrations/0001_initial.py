# Generated by Django 4.2.7 on 2023-11-29 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='действие')),
                ('description', models.TextField(blank=True, max_length=150, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'действие',
                'verbose_name_plural': 'действия',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='место')),
                ('description', models.TextField(blank=True, max_length=150, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'место',
                'verbose_name_plural': 'места',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='время и дата выполнения')),
                ('is_pleasure', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('periodicity', models.PositiveSmallIntegerField(default=1, verbose_name='периодичность в днях')),
                ('reward', models.CharField(blank=True, max_length=150, null=True, verbose_name='вознаграждение')),
                ('execution_time', models.PositiveSmallIntegerField(default=60, verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='habit', to='habit.action', verbose_name='действие')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='habit', to='habit.place', verbose_name='место')),
                ('pleasure_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='habit.habit', verbose_name='приятная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ('pk',),
            },
        ),
    ]
