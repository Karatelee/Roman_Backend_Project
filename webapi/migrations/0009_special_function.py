# Generated by Django 4.2.5 on 2023-09-23 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0008_orderdish_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='special_function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('calories', models.IntegerField(default=0)),
                ('carbohydrates', models.IntegerField(default=0)),
                ('proteins', models.IntegerField(default=0)),
                ('fats', models.IntegerField(default=0)),
                ('recipe', models.TextField(default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.typeofffood')),
            ],
            options={
                'verbose_name_plural': 'Dishes',
                'ordering': ['title'],
            },
        ),
    ]
