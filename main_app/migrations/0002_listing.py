# Generated by Django 2.2.12 on 2022-04-14 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market', models.CharField(max_length=15)),
                ('crypto', models.CharField(choices=[('B', 'Bitcoin'), ('E', 'Etherium'), ('S', 'Solana')], default='B', max_length=1)),
                ('nft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.NFT')),
            ],
        ),
    ]