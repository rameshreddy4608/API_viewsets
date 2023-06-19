from django.db import models

# Create your models here.

class product_category(models.Model):
    PCID=models.PositiveIntegerField()
    PCName=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.PCName
    

class product(models.Model):
    PCName=models.ForeignKey(product_category,on_delete=models.CASCADE)
    PID=models.IntegerField()
    Pname=models.CharField(max_length=100)
    Price=models.IntegerField()
    Pdate=models.DateField()

    def __str__(self) -> str:
        return self.Pname
