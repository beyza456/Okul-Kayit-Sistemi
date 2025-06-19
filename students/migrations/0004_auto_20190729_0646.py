# Bu dosya, Django uygulamasında veritabanı şemasını güncellemek için oluşturulan migration dosyasıdır.
# Burada, Attendance modelinde (student, date) alanlarının birlikte benzersiz (unique) olmasını sağlayan kısıtlama eklenir.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20190724_1545'),
    ]

   
    operations = [
      
       
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('student', 'date')},
        ),
    ]
