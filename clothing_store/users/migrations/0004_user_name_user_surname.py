# Generated by Django 4.2.3 on 2023-08-21 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_favorite_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default=2, max_length=120),
            preserve_default=False,
        ),
    ]
