# Bu dosya, Django uygulamasında veritabanı tablolarını (modelleri) tanımlamak için kullanılır.
# Result modeli, öğrencilerin sınav sonuçlarını (board, roll, gpa) veritabanında saklamak için oluşturulmuştur.

from django.db import models

# Create your models here.
class Result(models.Model):
    board = models.CharField(max_length=255)
    roll = models.IntegerField()
    gpa = models.IntegerField()

    def __str__(self):
      
        return str(self.roll)
