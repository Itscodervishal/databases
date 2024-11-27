from django.db import models

# Create your models here.
class stud(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    message=models.CharField(max_length=50)
    #create table stud(name varchar(50)),email varchar(50),mobile bright,msg varchar(20):

