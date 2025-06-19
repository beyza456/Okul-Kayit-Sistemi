# Bu dosya, Django uygulamasında veritabanı şemasını oluşturmak için kullanılan ilk (initial) migration dosyasıdır.
# Burada, Result adında bir modelin veritabanında tablo olarak oluşturulmasını sağlar.

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
     
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=255)),
                ('roll', models.IntegerField()),
                ('gpa', models.IntegerField()),
            ],
        ),
    ]
