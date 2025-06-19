# Bu dosya, Django uygulamasında veritabanı şemasını güncellemek için oluşturulan migration dosyasıdır.
# Burada, StudentClassInfo modeline class_short_form adında yeni bir alan (field) eklenmesini sağlar.

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20190729_0646'),
    ]

    
    
    operations = [
        migrations.AddField(
            model_name='studentclassinfo',
            name='class_short_form',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
