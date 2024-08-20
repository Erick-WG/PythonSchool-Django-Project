# Generated by Django 4.2.15 on 2024-08-20 08:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_student_date_of_birth'),
        ('teacher', '0003_remove_teacher_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='id',
        ),
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.CharField(default='address', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2024, 8, 20)),
        ),
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.CharField(default='department', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(default='phone_number', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(default='image', upload_to=''),
        ),
        migrations.AddField(
            model_name='teacher',
            name='salary',
            field=models.PositiveSmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='student_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_email',
            field=models.EmailField(default='email_address', max_length=254),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_first_name',
            field=models.CharField(default='first_name', max_length=40),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_last_name',
            field=models.CharField(default='last_name', max_length=40),
        ),
    ]
