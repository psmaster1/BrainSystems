from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=30)),
                ('house_type', models.CharField(max_length=100)),
                ('living_space', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('agreed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.URLField(blank=True, null=True)),
                ('page', models.CharField(choices=[('Index', 'Index'), ('Contact', 'Contact'), ('Login', 'Login'), ('Registration', 'Registration')], max_length=100, unique=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
