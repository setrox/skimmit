# Generated by Django 5.0 on 2023-12-23 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_model_choice_preference_ai_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preference',
            old_name='sentence_length',
            new_name='sentence_count',
        ),
    ]
