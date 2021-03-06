# Generated by Django 3.1.5 on 2021-01-25 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(editable=False, max_length=254)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Actived'), (1, 'Finished'), (2, 'Canceled'), (3, 'Deleted')], default=0)),
            ],
        ),
    ]
