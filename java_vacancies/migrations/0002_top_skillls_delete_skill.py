# Generated by Django 4.1.5 on 2023-01-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('java_vacancies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='top_skillls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]