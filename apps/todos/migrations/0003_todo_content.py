# Generated by Django 5.1.6 on 2025-02-27 11:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
