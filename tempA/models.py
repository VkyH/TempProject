from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='missing_persons',blank=True,null=True)

    def __str__(self):
        return self.name
