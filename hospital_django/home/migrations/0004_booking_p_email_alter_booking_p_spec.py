# Generated by Django 4.2.1 on 2023-06-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='p_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='p_spec',
            field=models.TextField(max_length=150),
        ),
    ]
