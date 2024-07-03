# Generated by Django 4.2.13 on 2024-07-03 10:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_account_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('transfer_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('transfer_type', models.CharField(blank=True, default='', max_length=15)),
                ('transfer_code', models.CharField(blank=True, default='', max_length=15)),
                ('transfer_charge', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('status', models.CharField(blank=True, default='', max_length=15)),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_received', to='accounts.account')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_sent', to='accounts.account')),
            ],
        ),
    ]
