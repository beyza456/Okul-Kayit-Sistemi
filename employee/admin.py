# Bu dosya, Django yönetici (admin) panelinde modellerin yönetilmesini sağlamak için kullanılır.
# OfficialInfo ve PersonalInfo modellerinin admin arayüzüne kaydedilmesini ve yönetici tarafından görüntülenip düzenlenebilmesini sağlar.


from django.contrib import admin
from .models import OfficialInfo, PersonalInfo

# Register your models here.
# admin.site.register(OfficialInfo)
# admin.site.register(PersonalInfo)

