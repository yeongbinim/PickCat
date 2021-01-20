<<<<<<< HEAD
# Generated by Django 3.1.5 on 2021-01-20 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainApps.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('phoneNumber', models.IntegerField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=mainApps.models.image_path)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', mainApps.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=20)),
                ('isNeutered', models.CharField(choices=[('T', 'TRUE'), ('F', 'FALSE'), ('U', 'UNKNOWN')], max_length=1)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('U', 'UNKNOWN')], max_length=1)),
                ('feature', models.TextField(blank=True, null=True)),
                ('registeredAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=mainApps.models.image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=mainApps.models.image_path)),
                ('checkIn', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('registeredAt', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KitchenMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mention', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApps.kitchen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mention', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApps.kitchen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CatPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('article', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApps.cat')),
            ],
        ),
        migrations.CreateModel(
            name='CatPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=mainApps.models.image_path)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApps.catpost')),
            ],
        ),
        migrations.CreateModel(
            name='CatMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mention', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApps.cat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cat',
            name='favoriteKitchen',
            field=models.ManyToManyField(to='mainApps.Kitchen'),
        ),
        migrations.AddField(
            model_name='user',
            name='favoriteCat',
            field=models.ManyToManyField(to='mainApps.Cat'),
        ),
        migrations.AddField(
            model_name='user',
            name='favoriteKitchen',
            field=models.ManyToManyField(to='mainApps.Kitchen'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
=======
>>>>>>> 4b261edb0f639092f970860bebf2a21824aaf810
