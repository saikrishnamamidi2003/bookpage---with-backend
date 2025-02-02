# Generated by Django 5.0.6 on 2024-05-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_product_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='Unknown Author', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='Unknown Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='No description available'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
