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

def run(): 
    ## to create new data u can also use the  
    restaurant = Restaurant() 
    Restaurant.objects.create(
        name='dominos pizza' , 
        date = timezone.now() , 
        restaurant_type = restaurant.TypeChoices.ITALIAN , 
        latitude = 0.32 , 
        longitude = 9.23
    )
    
# def run(): 
#     restaurant = Restaurant.objects.all() ## this function is to retreive the data from database 
#     # print(restaurant)   
#     get_1strow = Restaurant.objects.first() 
#     print("1st Row is := " , get_1strow)
#     print(connection.queries)
    
# if __name__ == '__main__': 
#     get_all_data()