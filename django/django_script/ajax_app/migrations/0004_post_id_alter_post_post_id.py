# Generated by Django 4.2.5 on 2023-10-31 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_app', '0003_alter_post_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.IntegerField(),
        ),
    ]
