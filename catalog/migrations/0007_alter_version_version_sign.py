# Generated by Django 4.2.4 on 2023-09-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_sign',
            field=models.BooleanField(choices=[(True, 'Активен'), (False, 'Неактивен')], default=True, verbose_name='Признак версий'),
        ),
    ]