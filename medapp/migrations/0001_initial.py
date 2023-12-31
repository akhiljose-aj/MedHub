# Generated by Django 4.2.5 on 2023-12-22 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=25)),
                ('admin_pass', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='appoint_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('date', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('department', models.CharField(max_length=25)),
                ('message', models.CharField(max_length=2000)),
                ('payment_id', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('Not_specified', 'NOT_SPECIFIED')], default='Not_specified', max_length=20)),
                ('status', models.CharField(choices=[('approve', 'approve'), ('reject', 'reject'), ('pending', 'pending')], default='pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='doctor_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=25)),
                ('doctor_id', models.IntegerField()),
                ('doctor_img', models.FileField(upload_to='')),
                ('doctor_dept', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('Not_specified', 'NOT_SPECIFIED')], default='Not_specified', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('gmail', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('Not_specified', 'NOT_SPECIFIED')], default='Not_specified', max_length=20)),
            ],
        ),
    ]
