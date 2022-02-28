# Generated by Django 4.0 on 2022-02-28 15:25

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_display_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('keywords', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=510, size=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'Disappointed'), (2, 'Unhappy'), (3, 'Works'), (4, 'Satisfied'), (5, 'Delighted')], help_text='How would you rate this business?')),
                ('description', models.TextField()),
                ('edited', models.BooleanField(default=b'I00\n')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='business/None/')),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.business')),
            ],
        ),
    ]
