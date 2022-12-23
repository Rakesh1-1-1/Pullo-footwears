# Generated by Django 4.1.4 on 2022-12-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0004_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=40)),
            ],
        ),
    ]
