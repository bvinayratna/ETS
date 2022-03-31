# Generated by Django 4.0.3 on 2022-03-30 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_delete_liked_songs'),
    ]

    operations = [
        migrations.CreateModel(
            name='liked_songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.CharField(max_length=250)),
                ('u_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='u_name', to='app.user', to_field='username')),
            ],
        ),
    ]