# Bu dosya, Django uygulamasının yapılandırma ayarlarını tanımlamak için kullanılır.
# Uygulamanın adı ve uygulama ile ilgili özel ayarlar burada belirlenir.


from django.apps import AppConfig


class EmployeeConfig(AppConfig):
    name = 'employee'
