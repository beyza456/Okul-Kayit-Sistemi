# Bu dosya, öğretmenlerle (teacher) ilgili veritabanı tablolarını (modelleri) tanımlar.
# TeacherDeptInfo, TeacherSubInfo ve TeacherInfo modelleri; öğretmenlerin bölüm, branş ve kişisel bilgilerini veritabanında saklamak amacıyla oluşturulmuştur.

from django.db import models

# Create your models here.
class TeacherDeptInfo(models.Model):
    dept_name = models.CharField(max_length=50)

    
    class Meta:
        verbose_name_plural = 'Department List'


    def __str__(self):
        
        return self.dept_name

class TeacherSubInfo(models.Model):
    sub_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Subject List'

    def __str__(self):
        return self.sub_name

class TeacherInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    teacher_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    passing_year = models.CharField(max_length=100)
    joining_date = models.DateField()
    dept_type = models.ForeignKey(TeacherDeptInfo, on_delete=models.CASCADE)
    sub_type = models.ForeignKey(TeacherSubInfo, on_delete=models.CASCADE)
    salary = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Teachers List'


    def __str__(self):
        return self.name

