# Generated by Django 4.0.3 on 2022-08-02 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_remove_plan_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='deadline',
            new_name='oxirgi_muddat',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='title',
            new_name='sarlavha',
        ),
    ]