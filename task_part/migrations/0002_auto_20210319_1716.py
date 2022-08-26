# Generated by Django 3.1.4 on 2021-03-19 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_part', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifymodel',
            name='status',
            field=models.CharField(choices=[('Done', 'Done'), ('Rejected', 'Rejected')], max_length=15),
        ),
        migrations.CreateModel(
            name='ApproveLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Done', 'Done'), ('Rejected', 'Rejected')], max_length=15)),
                ('leave_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_part.leavemodel')),
            ],
        ),
    ]