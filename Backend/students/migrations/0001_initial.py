# Generated by Django 3.1.4 on 2020-12-10 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        ('classrooms', '__first__'),
        ('schools', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroomID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='classrooms.classroom')),
                ('schoolID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='schools.school')),
                ('userID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='students.student')),
                ('subjectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject')),
            ],
        ),
    ]
