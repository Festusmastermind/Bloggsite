# Generated by Django 2.2 on 2020-02-19 02:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Education', 'Education'), ('Fashion', 'Fashion'), ('Arts', 'Arts'), ('Politics', 'Politics'), ('Sports', 'Sports'), ('Graphics', 'Graphics'), ('Programming', 'Programming'), ('Technologies', 'Technologies'), ('Entertainment', 'Entertainment'), ('Animation', 'Animation'), ('Business', 'Business'), ('others', 'others')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics'),
        ),
    ]
