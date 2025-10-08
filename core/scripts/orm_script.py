from core.models import Restaurant 
from django.utils import timezone
from django.db import connection  ## here it connect to database

# def run():  ## here we just add the data to it

#     restaurant = Restaurant() 
#     restaurant.name = "my indian Restaurant" 
#     restaurant.latitude = 40.9 
#     restaurant.longitude = 49.9  
#     restaurant.date  = timezone.now() 
#     restaurant.restaurant_type = Restaurant.TypeChoices.INDIAN 
    
#     restaurant.save() # it is responsible for save the data in the database
#     print("save the data")  

# def run(): 
#     ## to create new data u can also use the  
#     restaurant = Restaurant() 
#     Restaurant.objects.create(
#         name='biryani' , 
#         date = timezone.now() , 
#         restaurant_type = restaurant.TypeChoices.INDIAN , 
#         latitude = 83 , 
#         longitude = 23.2
#     ) 

# def run(): 
#     restaurant = Restaurant.objects.all()  
#     return_last_record = Restaurant.objects.last()  
#     count_of_rows_in_table = Restaurant.objects.count() 
#     print(f'Total record in table is {count_of_rows_in_table}')
#     print(f'last record in table is {return_last_record}')
#     print(restaurant) 
#     print()
#     print(connection.queries)
    
# def run(): 
#     restaurant = Restaurant.objects.all() ## this function is to retreive the data from database 
#     # print(restaurant)   
#     get_1strow = Restaurant.objects.first() 
#     print("1st Row is := " , get_1strow)
#     print(connection.queries)


# =======================  How we use the Foreign key to attached the table  in Django ================================= 

from django.contrib.auth.models import User 
from core.models import Restaurant , Rating
# def run():
#     restaurant = Restaurant.objects.first() 
#     user = User.objects.first() 

#     Rating.objects.create(user=user , restaurant=restaurant , rating=3) 
#     # after executing this if you go core_rating u will see  coulun is added to table where  restaurants column is there 


# =================== how to add  the filters on table ============================ 
# def run(): 
#     print(Rating.objects.filter(rating=3))
#     print(Rating.objects.filter(rating=5))   # this filter is just apply Where clause in query

# ======================  exclude on table =================== 
# def run(): 
#     print(Rating.objects.exclude(rating__lte=3))   ## here it just add where not in query

#     print(connection.queries) 

# ===================== updating the value in database ======================  
from pprint import pprint
def run(): 
    restaurant = Restaurant.objects.first() 

    restaurant.name  = "Rohit bhau restaurant" 
    restaurant.save() 
    pprint(connection.queries)