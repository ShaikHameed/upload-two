# Generated by Django 2.0.1 on 2018-01-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_paragraph_paragraph_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='paragraph_image',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
