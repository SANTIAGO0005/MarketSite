# Generated by Django 3.2.4 on 2022-07-20 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sales_CreatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice',
            name='DeleteBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sales_DeleteBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice',
            name='EnterpriceId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.bussines'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='ModifiyBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sales_ModifiyBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice',
            name='TaxId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.tax'),
        ),
    ]
