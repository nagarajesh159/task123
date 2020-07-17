# Generated by Django 2.2 on 2020-06-07 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Not started', 'Not started'), ('InProgress', 'InProgress'), ('Done', 'Done')], default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(choices=[('TL', 'Team Lead'), ('employee', 'employee')], max_length=10)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='task.Task')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
