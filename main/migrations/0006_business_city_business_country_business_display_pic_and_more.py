# Generated by Django 4.0 on 2022-03-22 11:54

from django.db import migrations, models
import django_mysql.models
import main.helper


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_business_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='city',
            field=models.CharField(blank=True, default='none', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='country',
            field=models.CharField(blank=True, default='none', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='display_pic',
            field=models.ImageField(blank=True, default='users/admin.jpg', null=True, upload_to=main.helper.saveDp),
        ),
        migrations.AddField(
            model_name='business',
            name='email',
            field=models.EmailField(default='vflstore', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='state',
            field=models.CharField(blank=True, default='none', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='keywords',
            field=django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=1275, size=25),
        ),
        migrations.AlterField(
            model_name='businessimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='businesses/None/'),
        ),
    ]
