# Generated by Django 3.1.7 on 2021-04-08 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0004_auto_20210409_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_vote',
            name='votes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polling.polls'),
        ),
    ]
