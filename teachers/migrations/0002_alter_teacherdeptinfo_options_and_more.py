# Bu dosya, Django uygulamasında veritabanı şemasını güncellemek için oluşturulan migration dosyasıdır.
# Burada, öğretmenlerle (teacher) ilgili modellerin admin panelinde görünen isimlerini (verbose_name_plural) günceller.
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        
      
        migrations.AlterModelOptions(
            name='teacherdeptinfo',
            options={'verbose_name_plural': 'Department List'},
        ),
        migrations.AlterModelOptions(
            name='teacherinfo',
            options={'verbose_name_plural': 'Teachers List'},
        ),
        migrations.AlterModelOptions(
            name='teachersubinfo',
            options={'verbose_name_plural': 'Subject List'},
        ),
    ]
