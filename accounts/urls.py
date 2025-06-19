# Bu dosya, Django uygulamasında kullanıcı giriş ve çıkış işlemleri için URL yönlendirmelerini tanımlar.
# Giriş ve çıkış işlemlerine ait view fonksiyonlarına erişim yolları burada belirlenir.

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

