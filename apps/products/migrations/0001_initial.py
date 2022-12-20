# Generated by Django 3.2 on 2022-12-20 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('crop_it', models.BooleanField(default=False, verbose_name='Crop It')),
                ('image', models.ImageField(blank=True, default='default/default_upload.jpg', upload_to='brand/images', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('crop_it', models.BooleanField(default=False, verbose_name='Crop It')),
                ('image', models.ImageField(blank=True, default='default/default_upload.jpg', upload_to='category/images', verbose_name='Image')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', related_query_name='children', to='products.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('crop_it', models.BooleanField(default=False, verbose_name='Crop It')),
                ('image', models.ImageField(blank=True, default='default/default_upload.jpg', null=True, upload_to='product/images', verbose_name='Image')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', related_query_name='product', to='products.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', related_query_name='product', to='products.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, verbose_name='Label')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta_field', related_query_name='meta_field', to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Meta Detail',
                'verbose_name_plural': "Product Meta Detail's",
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('crop_it', models.BooleanField(default=False, verbose_name='Crop It')),
                ('image', models.ImageField(blank=True, default='default/default_upload.jpg', upload_to='shop/images', verbose_name='Picture')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop', related_query_name='shop', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='Value')),
                ('product_meta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value', related_query_name='value', to='products.productmeta', verbose_name='Value')),
            ],
        ),
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='Ip Address')),
                ('hits', models.ManyToManyField(blank=True, related_name='hits', to='products.Category', verbose_name='Views')),
            ],
            options={
                'verbose_name': 'IP Address',
                'verbose_name_plural': 'IP Addressees',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/GalleryImage', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', related_query_name='images', to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('text', models.TextField(verbose_name='Text')),
                ('rate', models.IntegerField(verbose_name='Rate')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comments', to='products.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comments',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_product', related_query_name='shop_product', to='products.product', verbose_name='Product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_product', related_query_name='shop_product', to='products.shop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': 'Shop Product',
                'verbose_name_plural': 'Shop Products',
                'unique_together': {('shop', 'product')},
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.BooleanField(blank=True, verbose_name='Condition')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', related_query_name='likes', to='products.product', verbose_name='Products liked')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', related_query_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Like',
                'unique_together': {('user', 'products')},
            },
        ),
    ]