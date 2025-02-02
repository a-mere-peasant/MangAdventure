from django.db import migrations, models

from MangAdventure.models import RedditField


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='irc',
            field=models.CharField(
                blank=True, help_text="The group's IRC.", max_length=63
            ),
        ),
        migrations.AddField(
            model_name='group',
            name='reddit',
            field=RedditField(
                blank=True, max_length=24,
                help_text="The group's Reddit username or subreddit."
                " (Include /u/ or /r/)"),
        ),
        migrations.AddField(
            model_name='member',
            name='irc',
            field=models.CharField(
                blank=True, max_length=63,
                help_text="The member's IRC username."
            ),
        ),
        migrations.AddField(
            model_name='member',
            name='reddit',
            field=RedditField(
                blank=True, max_length=21,
                help_text="The member's Reddit username."
            ),
        ),
        migrations.AlterField(
            model_name='group',
            name='website',
            field=models.URLField(blank=True, help_text="The group's website."),
        ),
    ]
