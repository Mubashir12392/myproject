# Generated by Django 5.0.3 on 2024-03-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=50)),
                ('teacher_age', models.IntegerField(default=0)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
            ],
        ),
    ]
