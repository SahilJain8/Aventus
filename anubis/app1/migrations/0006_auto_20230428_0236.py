# Generated by Django 3.2.18 on 2023-04-28 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_delete_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='managerid',
        ),
        migrations.DeleteModel(
            name='Hr',
        ),
        migrations.DeleteModel(
            name='Managers',
        ),
        migrations.RemoveField(
            model_name='points',
            name='employeeid',
        ),
        migrations.RemoveField(
            model_name='points',
            name='rewardid',
        ),
        migrations.RemoveField(
            model_name='points',
            name='senderid',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.DeleteModel(
            name='Points',
        ),
        migrations.DeleteModel(
            name='Rewards',
        ),
    ]
