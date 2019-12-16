from django.db import models
"""from pygments.lexers import get_all_lexers  # for highlighting some special output
from pygments.styles import get_all_styles  # for highlighting some special output"""
import datetime


"""# for highlighting some special output
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])"""





# Create your models here.
class Customer(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    # customer_name
    name = models.CharField(max_length=255, null=False)
    # customer id
    cust_id = models.IntegerField(null=False)
    # rate of water jar for this customer
    cust_rate = models.IntegerField(null=False,default=20)
    # a counter for daily updation in a month
    
    number_of_jars_taken_in_a_month = models.IntegerField(null=False,default=0)
    
    """def __str__(self):
        return "{} - {}".format(self.name, self.cust_id)"""
    class meta:
        ordering = ['created']