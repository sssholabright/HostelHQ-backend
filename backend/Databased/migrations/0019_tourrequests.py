# Generated by Django 5.0.1 on 2024-08-10 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Databased', '0018_agentlisting_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_date', models.DateField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined')], default='PENDING', max_length=10)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_requests', to='Databased.userprofile')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_requests', to='Databased.userprofile')),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Databased.agentlisting')),
            ],
        ),
    ]
