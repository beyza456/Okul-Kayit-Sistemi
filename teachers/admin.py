# Bu dosya, öğretmenlerle (teacher) ilgili modellerin Django yönetici (admin) panelinde yönetilmesini sağlar.
# Modellerin admin arayüzüne kaydedilmesini ve yönetici tarafından görüntülenip düzenlenebilmesini sağlar.

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TeacherDeptInfo)
admin.site.register(TeacherSubInfo)
admin.site.register(TeacherInfo)

