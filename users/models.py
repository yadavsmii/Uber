from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=15,null=True,blank=True)
    surname = models.CharField(max_length=15,null=True,blank=True)
    birth = models.DateField(max_length=10,null=True,blank=True)
    mobile_number = models.IntegerField(max_length=10,null=True,blank=True)
    GENDER_TYPES = (
        (1,'Female'),
        (2,'Male'),
        (3,'Others'),
    )
    gender_type = models.IntegerField(
        choices=GENDER_TYPES,
    )
    def __str__(self):
        return str(self.first_name)

class Orders(models.Model):
    order_name = models.CharField(max_length=15,null=True,blank=True)
    order_price = models.IntegerField(max_length=15,null=True,blank=True)
    order_discount = models.IntegerField(max_length=15,null=True,blank=True)
    order_quantity = models.IntegerField(max_length=15,null=True,blank=True)
    order_address = models.TextField(max_length=15,null=True,blank=True)
    order_place_at = models.DateField(max_length=15,null=True,blank=True)


class StudentsAddress(models.Model):
    Students=models.ForeignKey(Students,on_delete=models.CASCADE,null=True,related_name="students_addresses")
    street_name = models.CharField(max_length=15,null=True,blank=True)
    house_number = models.IntegerField(max_length=15,null=True,blank=True)
    city = models.CharField(max_length=15,null=True,blank=True)
    state = models.CharField(max_length=15,null=True,blank=True)
    country= models.CharField(max_length=15,null=True,blank=True)
    pin_code = models.IntegerField(max_length=15,null=True,blank=True)
    
    def __str__(self):
        return str(self.street_name)

    



