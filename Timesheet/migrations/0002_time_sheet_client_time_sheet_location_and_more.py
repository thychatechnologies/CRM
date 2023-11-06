# Generated by Django 4.2.4 on 2023-11-04 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0001_initial'),
        ('Timesheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='time_sheet',
            name='Client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Clients.client'),
        ),
        migrations.AddField(
            model_name='time_sheet',
            name='Location',
            field=models.CharField(choices=[('Office', 'Office'), ('Work From Home', 'Work From Home')], default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='time_sheet',
            name='Mode',
            field=models.CharField(choices=[('New', 'New'), ('Rework', 'Rework'), ('Edit', 'Edit')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='time_sheet',
            name='Type',
            field=models.CharField(choices=[('Other', 'Other'), ('Poster', 'Poster'), ('Video', 'Video'), ('Branding', 'Branding'), ('Brochure', 'Brochure'), ('Packaging', 'Packaging'), ('Developing', 'Developing')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
