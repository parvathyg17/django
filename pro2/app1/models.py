from django.db import models

# Create your models here.
class employee(models.Model):
    e_id=models.IntegerField()
    ename=models.CharField(max_length=20)
    emp_dep=models.CharField(max_length=10)
    emp_salary=models.IntegerField()