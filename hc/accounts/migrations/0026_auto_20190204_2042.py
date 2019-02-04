# Generated by Django 2.1.5 on 2019-02-04 20:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_remove_member_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='api_key',
            field=models.CharField(blank=True, db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='project',
            name='api_key_readonly',
            field=models.CharField(blank=True, db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
