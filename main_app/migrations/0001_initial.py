# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 11:00
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_type', models.IntegerField(choices=[(1, 'Like'), (2, 'Favorite')])),
                ('ip_address', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField()),
                ('body_en', ckeditor.fields.RichTextField(null=True)),
                ('body_ru', ckeditor.fields.RichTextField(null=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='images/base')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('name_en', models.CharField(max_length=40, null=True)),
                ('name_ru', models.CharField(max_length=40, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('desc', models.TextField()),
                ('desc_en', models.TextField(null=True)),
                ('desc_ru', models.TextField(null=True)),
                ('type', models.IntegerField(choices=[(1, 'Insert'), (2, 'Accessory')])),
                ('price_byn', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=5)),
                ('base_image', imagekit.models.fields.ProcessedImageField(default='media/default.png', upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(default='media/default.png', upload_to='images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main_app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=40)),
                ('key_expires', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='main_app.Product'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
