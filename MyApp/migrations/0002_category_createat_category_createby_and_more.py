# Generated by Django 4.2.4 on 2023-09-13 16:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='createAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='createBy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updateAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updateBy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('barcode', models.BigIntegerField(null=True, unique=True)),
                ('unitPrice', models.FloatField()),
                ('qtyInstock', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Product/')),
                ('createBy', models.IntegerField(blank=True, null=True)),
                ('updateBy', models.IntegerField(blank=True, null=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.category')),
            ],
        ),
    ]
