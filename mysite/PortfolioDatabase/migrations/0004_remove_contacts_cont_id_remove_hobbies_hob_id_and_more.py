# Generated by Django 4.2.5 on 2023-10-16 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0003_contacts_hobbies_hob_id_portfolio_port_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='cont_id',
        ),
        migrations.RemoveField(
            model_name='hobbies',
            name='hob_id',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='port_id',
        ),
    ]
