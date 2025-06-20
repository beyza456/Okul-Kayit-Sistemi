# Bu dosya, Django uygulamasında veritabanı şemasını oluşturmak için kullanılan ilk (initial) migration dosyasıdır.
# Burada, öğretmenlerle (teacher) ilgili ana modellerin (TeacherDeptInfo, TeacherSubInfo, TeacherInfo) veritabanında tablo olarak oluşturulmasını sağlar.

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherDeptInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSubInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('teacher_img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('passing_year', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
                ('salary', models.IntegerField()),
                ('dept_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.TeacherDeptInfo')),
                ('sub_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.TeacherSubInfo')),
            ],
        ),
    ]
