# Generated by Django 2.0.7 on 2020-08-28 19:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Създадено на'),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Последен ъпдейт'),
        ),
    ]
