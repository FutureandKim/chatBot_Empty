# Generated by Django 4.2.1 on 2023-06-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=16, unique=True, verbose_name='이름')),
                ('user_birth', models.DateField(verbose_name='생년월일')),
            ],
            options={
                'verbose_name': '이름',
                'verbose_name_plural': '이름',
                'db_table': 'name',
            },
        ),
    ]
