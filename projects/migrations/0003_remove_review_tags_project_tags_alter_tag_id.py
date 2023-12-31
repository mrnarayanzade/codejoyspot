# Generated by Django 4.0.4 on 2023-12-17 16:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_alter_project_id_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='tags',
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projects.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
