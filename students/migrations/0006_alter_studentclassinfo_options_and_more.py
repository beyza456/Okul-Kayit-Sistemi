# Bu dosya, Django uygulamasında veritabanı şemasını güncellemek için oluşturulan migration dosyasıdır.
# Burada, öğrenciyle ilgili modellerin admin panelinde görünen isimlerini (verbose_name_plural) günceller.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_studentclassinfo_class_short_form'),
    ]

   
    operations = [
      
     
        migrations.AlterModelOptions(
            name='studentclassinfo',
            options={'verbose_name_plural': 'Class List'},
        ),
        migrations.AlterModelOptions(
            name='studentinfo',
            options={'verbose_name_plural': 'Student List'},
        ),
        migrations.AlterModelOptions(
            name='studentsectioninfo',
            options={'verbose_name_plural': 'Section List'},
        ),
        migrations.AlterModelOptions(
            name='studentshiftinfo',
            options={'verbose_name_plural': 'Shift List'},
        ),
    ]
