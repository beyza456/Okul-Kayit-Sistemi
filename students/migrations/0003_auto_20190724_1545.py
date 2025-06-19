# Bu dosya, Django uygulamasında veritabanı şemasını güncellemek için oluşturulan migration dosyasıdır.
# Burada, StudentInfo modelinde (admission_id, class_type) alanlarının birlikte benzersiz (unique) olmasını sağlayan kısıtlama eklenir.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_attendance'),
    ]

   
    operations = [
        
       
        migrations.AlterUniqueTogether(
            name='studentinfo',
            unique_together={('admission_id', 'class_type')},
        ),
    ]
