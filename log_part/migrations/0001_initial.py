# Generated by Django 3.1.4 on 2021-03-16 12:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpt_name', models.CharField(max_length=100, unique=True)),
                ('dpt_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_picture', models.ImageField(upload_to='EmployeeProfileModel/emp_pic')),
                ('emp_contact', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+?(88)01[3-9][0-9]{8}$')], verbose_name="Employee's Mobile phone")),
                ('Date_of_Birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('Female', 'Female'), ('Third Gender', 'Third Gender')], max_length=15)),
                ('emp_nid', models.IntegerField()),
                ('emp_address', models.CharField(max_length=200)),
                ('e_resume', models.ImageField(upload_to='EmployeeProfileModel/E_resume')),
                ('emp_id', models.CharField(max_length=50, unique=True)),
                ('emp_designation', models.CharField(max_length=100)),
                ('emp_salary', models.IntegerField()),
                ('emp_assigned_leaves', models.IntegerField()),
                ('joining_date', models.DateField()),
                ('emp_dpt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp_dpt', to='log_part.departmentmodel')),
                ('emp_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='emp_name', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='manager_of_epm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_of_dpt', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='head_of_dpt', to='log_part.departmentmodel')),
                ('mgr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mgr_id', to='log_part.employeeprofilemodel')),
                ('mgr_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mgr_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
