# Generated by Django 2.2 on 2023-08-09 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0006_auto_20230807_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.CharField(default='', max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisements.AdvertisementStatus', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Заголовок'),
        ),
    ]