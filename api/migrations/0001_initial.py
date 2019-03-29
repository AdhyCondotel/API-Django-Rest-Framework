# Generated by Django 2.0 on 2019-03-29 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('as_address', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('keluarahan', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('duration', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_rate', models.FloatField(blank=True, default=0.0, null=True)),
                ('message', models.TextField(default='', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('delivery', models.BooleanField()),
                ('status', models.BooleanField()),
                ('photo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('role', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=225)),
                ('photo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='tenant',
            name='users_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenant', to='api.User'),
        ),
        migrations.AddField(
            model_name='rate',
            name='tenant_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_tenant', to='api.Tenant'),
        ),
        migrations.AddField(
            model_name='rate',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='price',
            name='tenant_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price', to='api.Tenant'),
        ),
    ]
