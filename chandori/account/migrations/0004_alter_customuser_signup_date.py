# Generated by Django 3.2.6 on 2021-08-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='signup_date',
            field=models.DateTimeField(null=True),
        ),
    ]