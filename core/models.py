from django.db import models
from django.contrib.auth.models import User  
# Create your models here. 

# we creating the table Restaurant , User , Rating.
class Restaurant(models.Model): 
    
    class TypeChoices(models.TextChoices):  
        # by defining the this class we can only choose from this 
        INDIAN = 'IN' , 'India' 
        CHINESE = 'CH' , 'Chinese' 
        ITALIAN = 'IT' , 'Italian' 
        GREEK = 'GR' , 'Greek' 
        MEXICAN = 'MX' , 'Mexican' 
        FASTFOOD = 'FF' , 'Fast Food' 
        OTHER = 'OT' , 'Other' 
        
        
    name = models.CharField(max_length=100) 
    website = models.URLField(default='' , max_length=100)
    date = models.DateField() 
    latitude = models.FloatField() 
    longitude = models.FloatField() 
    restaurant_type = models.CharField(max_length=2 , choices=TypeChoices.choices)
    def __str__(self):
        return self.name 
    
## user come builtin with django so we can not create but we can create our own 

class Rating(models.Model): 
    user = models.ForeignKey(User,# user is the Table which foreign key refers , 
                             on_delete=models.CASCADE # if User table get deleted we also delete connection with Rating table 
                             ) 
    restaurant = models.ForeignKey(Restaurant , 
                                   on_delete=models.CASCADE) 
    rating = models.PositiveSmallIntegerField() 

    def __str__(self):
        return f"Rating : {self.rating}" 
    
class Sale(models.Model): 
    restaurant = models.ForeignKey(Restaurant , on_delete=models.SET_NULL , null=True) 
    income = models.DecimalField(max_digits=6 , decimal_places=2)  
    datetime = models.DateTimeField()
    
    def __str__(self):
        return f'Sale : {self.income}'