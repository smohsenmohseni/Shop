# Generated by Django 3.1.4 on 2021-02-02 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shop', related_query_name='shop', to='app_account.user', verbose_name='Owner'),
            preserve_default=False,
        ),
    ]