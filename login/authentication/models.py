from django.db import models

# Create your models here.
class Upload(models.Model):
    name=models.CharField( max_length=122)
    reportNumber=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    age=models.IntegerField() 
    mri= models.ImageField(upload_to="authentication/images",default="")
    def __str__(self):
        return self.name