# Generated by Django 5.0.7 on 2024-07-15 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_demo_link_alter_project_source_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
    ]
