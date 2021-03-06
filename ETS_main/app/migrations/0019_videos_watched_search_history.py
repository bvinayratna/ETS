# Generated by Django 4.0.3 on 2022-03-31 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_liked_songs_album_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='videos_watched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=250)),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.PROTECT, to='app.user', to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='search_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_query', models.CharField(max_length=250)),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.PROTECT, to='app.user', to_field='username')),
            ],
        ),
    ]
