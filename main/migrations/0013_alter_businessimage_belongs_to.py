# Generated by Django 4.0 on 2022-03-26 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_business_display_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessimage',
            name='belongs_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has', to='main.business'),
        ),
    ]