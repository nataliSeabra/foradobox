# Generated by Django 2.1.5 on 2019-08-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutMe', '0004_auto_20190813_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='experience',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Position'),
        ),
        migrations.AlterUniqueTogether(
            name='experience',
            unique_together=set(),
        ),
    ]
