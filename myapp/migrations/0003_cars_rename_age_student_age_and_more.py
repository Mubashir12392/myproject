# Generated by Django 5.0.3 on 2024-03-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=50)),
                ('car_colour', models.CharField(choices=[('red', 'Red'), ('yellow', 'Yellow'), ('blue', 'Blue'), ('black', 'Black')], max_length=50)),
                ('car_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Gender',
            new_name='gender',
        ),
    ]