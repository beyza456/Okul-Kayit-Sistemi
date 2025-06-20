# Bu dosya, Django uygulamasında veritabanı şemasını güncellemek için oluşturulan migration dosyasıdır.
# Burada, OfficialInfo ve PersonalInfo adında iki yeni modelin veritabanında tablo olarak oluşturulmasını sağlar.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    
    operations = [
        
        migrations.CreateModel(
            name='OfficialInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_register_number', models.CharField(max_length=20)),
                ('official_register_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('another_fullname', models.CharField(max_length=100)),
                ('national_id', models.IntegerField()),
                ('employee_avatar', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
