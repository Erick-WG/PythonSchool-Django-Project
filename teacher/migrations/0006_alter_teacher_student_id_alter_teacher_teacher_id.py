# Generated by Django 4.2.15 on 2024-08-20 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_student_date_of_birth'),
        ('teacher', '0005_remove_teacher_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
