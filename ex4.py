cars = 100
space_is_a_car = 4.0
drivers =30
passenger = 90
cars_not_driven =  cars - drivers
car_driven = drivers
carpool_capacity = car_driven * space_is_a_car
average_passenger_per_car = passenger / car_driven

#print how many cars avalable
print("there are ",cars," cars available")
print("there are only ", drivers , " drivers available")
print("there will be ", cars_not_driven , "empty cars today")
print("we can transport ", carpool_capacity , " people today")
print("we have ",passenger," passenger to carpool today")
print("we have to put about ",average_passenger_per_car,
                                        "passenger in each car")
