from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_data_file', models.FileField(upload_to='')),
                ('intents_json_file', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
