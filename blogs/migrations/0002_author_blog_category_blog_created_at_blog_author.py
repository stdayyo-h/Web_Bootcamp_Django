# Generated by Django 4.1.7 on 2023-03-25 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('TC', 'Technical'), ('LF', 'Lifestyle'), ('SP', 'Sports'), ('FD', 'Food')], default='TC', max_length=2),
        ),
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.author'),
        ),
    ]
