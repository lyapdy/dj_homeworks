from django.db import models



class Phone(models.Model):
   
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    image = models.ImageField()
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length = 200, unique=True)
    
