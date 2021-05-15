# Generated by Django 3.2.2 on 2021-05-15 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0001_initial'),
        ('product', '0002_alter_product_p_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='p_type',
        ),
        migrations.AddField(
            model_name='product',
            name='p_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='type.type'),
        ),
    ]
