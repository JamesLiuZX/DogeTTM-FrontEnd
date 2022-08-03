# Generated by Django 4.0.5 on 2022-08-03 09:15

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('address', models.CharField(max_length=42, unique=True)),
                ('owners', models.BigIntegerField(default=0)),
                ('token_count', models.BigIntegerField(default=0)),
                ('avg_price', models.JSONField(default=dict)),
                ('max_price', models.JSONField(default=dict)),
                ('sales_count', models.JSONField(default=dict)),
                ('sales_volume', models.JSONField(default=dict)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('tkn', models.JSONField()),
                ('prc', models.JSONField()),
                ('vol', models.JSONField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NFT.collection')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_id', models.DecimalField(decimal_places=0, default=Decimal('0.00'), max_digits=10)),
                ('type', models.CharField(choices=[('encoded', 'Encoded'), ('url', 'URL')], default='url', max_length=7)),
                ('data', models.TextField(default='', max_length=100000)),
                ('mimeType', models.CharField(default='', max_length=50)),
                ('parent_collection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='NFT.collection')),
            ],
        ),
        migrations.AddConstraint(
            model_name='datapoint',
            constraint=models.UniqueConstraint(fields=('collection', 'timestamp'), name='nft_datapoint_unique'),
        ),
    ]
