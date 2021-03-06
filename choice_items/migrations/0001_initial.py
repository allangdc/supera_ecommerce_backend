# Generated by Django 4.0.4 on 2022-06-04 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_items', '0001_initial'),
        ('wishlist', '0005_wishlist_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_items.storeitems')),
                ('id_wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wishlist.wishlist')),
            ],
        ),
    ]
