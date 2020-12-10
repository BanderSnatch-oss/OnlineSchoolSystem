# Generated by Django 3.1.4 on 2020-12-10 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('schedule', models.JSONField(default=dict)),
                ('schoolID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='schools.school')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects_Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroomID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='classrooms.classroom')),
                ('subjectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject')),
            ],
        ),
    ]
