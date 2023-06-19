# Generated by Django 4.2.2 on 2023-06-19 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PCID', models.PositiveIntegerField()),
                ('PCName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.IntegerField()),
                ('Pname', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Pdate', models.DateField()),
                ('PCName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_category')),
            ],
        ),
    ]
