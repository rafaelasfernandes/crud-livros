# Generated by Django 2.1.7 on 2019-03-14 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('ISBN', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=60)),
                ('ano', models.IntegerField()),
                ('editora', models.CharField(max_length=60)),
            ],
        ),
    ]