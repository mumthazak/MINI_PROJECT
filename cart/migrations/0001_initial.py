# Generated by Django 3.2.15 on 2022-11-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cart',
                'managed': False,
            },
        ),
    ]
