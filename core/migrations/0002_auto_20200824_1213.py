# Generated by Django 3.1 on 2020-08-24 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Unknown'), (1, 'World of Warcraft'), (3, 'League of Legends'), (2, 'Conter-Strike')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
    ]