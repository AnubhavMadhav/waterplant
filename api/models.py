from django.db import models

# Create your models here.
class Customers(models.Model):
    # customer_name
    name = models.CharField(max_length=255, null=False)
    # customer id
    cust_id = models.IntegerField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.cust_id)
