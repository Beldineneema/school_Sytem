# Generated by Django 3.2.5 on 2021-07-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=10)),
                ('Age', models.PositiveSmallIntegerField()),
                ('Date_of_birth', models.DateField()),
            ],
        ),
    ]
