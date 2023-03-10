# Generated by Django 4.1.5 on 2023-01-31 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Country Name')),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=3, unique=True, verbose_name='Currency')),
            ],
            options={
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Sector')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Signature date')),
                ('title', models.CharField(max_length=250)),
                ('amount', models.IntegerField(verbose_name='Signed amount')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.country')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.currency')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.sector')),
            ],
        ),
    ]
