# Generated by Django 2.2 on 2020-04-16 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('s_time', models.PositiveIntegerField(default=0)),
                ('num', models.PositiveIntegerField(default=30)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('time', models.PositiveIntegerField(default=0)),
                ('grade', models.PositiveIntegerField(default=0)),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
                ('word_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Word')),
            ],
        ),
    ]
