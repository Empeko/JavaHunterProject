# Generated by Django 4.1.5 on 2023-01-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('java_vacancies', '0005_geography_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('aver_salary', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='geography_model',
        ),
    ]
