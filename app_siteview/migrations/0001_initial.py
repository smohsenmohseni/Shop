# Generated by Django 3.1.4 on 2021-02-07 19:09

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShowImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_text', models.CharField(max_length=35, verbose_name='Action Text')),
                ('action_url', models.URLField(verbose_name='Action Url')),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
                ('crop_it', models.BooleanField(default=False, verbose_name='Crop It')),
                ('image', models.ImageField(upload_to='slideShowPictures/images', verbose_name='Background')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '530x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping')),
                ('end_time', models.DateTimeField(verbose_name='End At')),
            ],
            options={
                'verbose_name': 'Slide Show',
                'verbose_name_plural': 'Slide Shows',
            },
        ),
    ]
