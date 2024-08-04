# Generated by Django 5.0.1 on 2024-08-03 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Databased', '0016_alter_userprofile_name_alter_userprofile_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='agentlisting',
            name='images',
            field=models.ManyToManyField(blank=True, to='Databased.image'),
        ),
        migrations.DeleteModel(
            name='AgentListingImage',
        ),
    ]
