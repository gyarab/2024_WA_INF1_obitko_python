# Generated by Django 5.1.6 on 2025-03-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RemoveField(
            model_name='song',
            name='key',
        ),
        migrations.RemoveField(
            model_name='song',
            name='name',
        ),
        migrations.RemoveField(
            model_name='song',
            name='tempo',
        ),
        migrations.AddField(
            model_name='song',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='chordpro/'),
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
