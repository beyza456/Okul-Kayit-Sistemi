# Bu dosya, Django uygulamasında API endpoint'leri için URL yönlendirmelerini tanımlar.
# Öğrenci yoklama, sonuç ve öğrenci oluşturma işlemlerine ait view sınıflarına erişim yolları burada belirlenir.

from django.urls import path
from . import views

urlpatterns = [
    path('attendance/<student_class>/<student_id>', views.StudentAttendance.as_view(), name='student_attendance'),
    path('result', views.ResultInfo.as_view(), name='result'),
    path('student/create', views.CreateStudentInfo.as_view()),
]

