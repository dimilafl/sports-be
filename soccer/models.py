from django.db import models

# Create your models here.


class Soccer(models.Model):
    squad = models.CharField(max_length=100, default='no value')
    age = models.CharField(max_length=100 , default='no value')
    poss = models.CharField(max_length=100 , default='no value')
    mp = models.CharField(max_length=100 , default='no value')
    starts = models.CharField(max_length=100 , default='no value')
    minutes = models.CharField(max_length=100 , default='no value')
    nineties = models.CharField(max_length=100 , default='no value')
    gls = models.CharField(max_length=100 , default='no value')
    ast = models.CharField(max_length=100 , default='no value')

    # g_minus_pk = models.CharField(max_length=100)

    # team = models.CharField(max_length=100)
    # photo_url = models.CharField(max_length=200, null=True)
    
    # # title = models.CharField(max_length=100, default='no song title')
    

    def __str__(self):
        return self.squad



class Statistic(models.Model):
    soccer = models.ForeignKey(Soccer, on_delete=models.CASCADE, related_name='statistics')

    def save(self, *args, **kwargs):
        # self.total_price = self.price * self.quantity
        super().save(*args,**kwargs)

    # possession = models.CharField(max_length=100 , default='no value')

    
#     preview_url = models.CharField(max_length=200, null=True)
    
#     name = models.CharField(max_length=100, default='no name ')
#     wins = models.CharField(max_length=100, default='empty value')
#     losses = models.CharField(max_length=100, default='empty value')
#     draws = models.CharField(max_length=100, default='empty value')
    

#     # title = models.CharField(max_length=100, default='no song title')
#     # album = models.CharField(max_length=100, default='no album title')
#     # nationality = models.CharField(max_length=100)