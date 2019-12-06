# Generated by Django 2.2.7 on 2019-12-03 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Squirrel_Sightings', '0003_auto_20191203_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrels',
            name='Age',
            field=models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('', ''), ('?', '?')], help_text='Age', max_length=50),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Approaches',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Approaches', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Chasing',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Chasing', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Climbing',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Climbing', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Date',
            field=models.DateField(help_text='Date'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Eating',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Eeating', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Foraging',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Foraging', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Indifferent',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Indifferent', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Kuks',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Kuks', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Latitude',
            field=models.FloatField(help_text='Latitude'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Location',
            field=models.CharField(choices=[('ground plane', ' Ground Plane'), ('above ground', 'Above Ground'), ('other', 'Other')], default='other', help_text='Location', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Longitude',
            field=models.FloatField(help_text='Longitude'),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Moans',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Moan', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Other_Activities',
            field=models.CharField(help_text='Other activities', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Primary_Fur_Color',
            field=models.CharField(choices=[('black', 'Black'), ('cinnamon', 'Cinnamon'), ('gray', 'Gray')], help_text='Primary Fur Color', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Quaas',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Quaas', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Running',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Running', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Runs_from',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Run from', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift', max_length=2),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Tail_flags',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Tail Flags', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Tail_twitches',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Tail Twitch', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrels',
            name='Unique_Squirrel_Id',
            field=models.CharField(help_text='Unique Squirrel ID', max_length=30),
        ),
    ]