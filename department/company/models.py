from django.db import models

# Create your models here.
#Департамент содержит: Название Связь с сотрудником - директором департаментаДолжна быть обеспечена уникальности связки “сотрудник-департамент”. 

class Department(models.Model):
    name = models.CharField(max_length=40)
    manager = models.OneToOneField("company.Person", null=True, blank=True, on_delete=models.CASCADE)

#Модель данных:Сотрудник содержит атрибуты: ФИО Фото Должность Оклад Возраст Департамент

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40, db_index=True)
    outer_name = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    salary_size = models.FloatField()
    age = models.IntegerField()
    depatrment = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)

