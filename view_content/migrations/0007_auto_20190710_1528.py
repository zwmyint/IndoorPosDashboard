# Generated by Django 2.2.3 on 2019-07-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_content', '0006_taglocations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='vx',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='vy',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='x_pos',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='y_pos',
        ),
        migrations.AddField(
            model_name='taglocations',
            name='timestamp',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='taglocations',
            name='vx',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='taglocations',
            name='vy',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='taglocations',
            name='x_pos',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='taglocations',
            name='y_pos',
            field=models.FloatField(default=0),
        ),
    ]
