# Generated by Django 4.2.4 on 2023-11-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.AddField(
            model_name='user',
            name='Department',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Image',
            field=models.ImageField(null=True, upload_to='Team'),
        ),
        migrations.AddField(
            model_name='user',
            name='Job_Role',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Mobile',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Staff_ID',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]