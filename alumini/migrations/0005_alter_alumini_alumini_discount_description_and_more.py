# Generated by Django 5.1.2 on 2024-10-22 21:21

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumini', '0004_alter_alumini_id_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumini',
            name='alumini_discount_description',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Alumini Discount Description'),
        ),
        migrations.AlterField(
            model_name='alumini',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]