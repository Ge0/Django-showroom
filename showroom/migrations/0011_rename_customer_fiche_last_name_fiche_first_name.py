# Generated by Django 4.0 on 2022-01-28 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0010_fiche_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fiche',
            old_name='customer',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='fiche',
            name='first_name',
            field=models.CharField(default='client', max_length=200),
            preserve_default=False,
        ),
    ]
