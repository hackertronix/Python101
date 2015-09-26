def hotel_cost(nights):
    return 140*nights
    
    
def plane_ride_cost(city):
    if(city=="Charlotte"):
        return 183
    elif(city=="Las Vegas"):
        return 227
    elif(city=="New York City"):
        return 299
    elif(city=="Los Angeles"):
        return 370
    
def rental_car_cost(days):
    cost =days*40
    if(days>=7):
        return cost-50
    elif(days>=3 and days<7):
        return cost-20
    else:
        return cost
    
def trip_cost(city,days,spending_money):
    total=spending_money+hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)
    return total
print trip_cost("Los Angeles",5,600)