# Generated by Django 5.0 on 2023-12-22 18:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_summary', '0002_alter_urlsummary_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='urlsummary',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_summaries', to=settings.AUTH_USER_MODEL),
        ),
    ]