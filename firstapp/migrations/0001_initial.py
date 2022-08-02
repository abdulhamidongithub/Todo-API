# Generated by Django 4.0.3 on 2022-03-02 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('matn', models.TextField(blank=True)),
                ('deadline', models.DateTimeField()),
                ('holat', models.CharField(choices=[('Yangi', 'Yangi'), ('Davom etyapti', 'Davom etyapti'), ('Bajarilgan', 'Bajarilgan')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
