# Generated by Django 4.0.3 on 2023-03-15 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_rest', '0006_remove_user_join_date_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='!wqYYirK8c8WfBXoZ4F7GfGFRAEK4Iov7zZZT4qid', max_length=128),
        ),
    ]
