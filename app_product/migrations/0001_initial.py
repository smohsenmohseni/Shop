# Generated by Django 3.1.4 on 2021-01-09 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('image', models.ImageField(blank=True, upload_to='brand/images', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('image', models.ImageField(blank=True, upload_to='category/images', verbose_name='Image')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', related_query_name='children', to='app_product.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/images', verbose_name='Image')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', related_query_name='product', to='app_product.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', related_query_name='product', to='app_product.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Shop')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to='shop/images', verbose_name='Picture')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
            },
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_product', related_query_name='shop_product', to='app_product.product', verbose_name='Product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_product', related_query_name='shop_product', to='app_product.shop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': 'Shop Product',
                'verbose_name_plural': 'Shop Products',
            },
        ),
        migrations.CreateModel(
            name='ProductMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, verbose_name='Label')),
                ('value', models.CharField(max_length=100, verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta_field', related_query_name='meta_field', to='app_product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Meta Data',
                'verbose_name_plural': 'Product Meta Detail',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/GalleryImage', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', related_query_name='images', to='app_product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('rate', models.IntegerField(verbose_name='Rate')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comments', to='app_product.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comments',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.BooleanField(blank=True, verbose_name='Condition')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', related_query_name='likes', to='app_product.product', verbose_name='Products liked')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', related_query_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Like',
                'unique_together': {('user', 'condition')},
            },
        ),
    ]
