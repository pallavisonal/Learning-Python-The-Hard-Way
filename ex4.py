cars = 100;
space_in_a_car = 4;
drivers = 30;
passengers = 90;
cars_not_driven = cars - drivers;
cars_driven = drivers;
carpool_capacity = space_in_a_car * cars_driven;
average_passengers_per_car = passengers / cars_driven;
# $ not permitted at start, number not permitted at the beginning
#$my_apples = 20;
#1my_apples = 20;

# $ not permitted at any place
#my_$apples = 20;
#numbers permitted in middle or end
my_1apples1 = 20;

print ("There are", cars, "cars available.");
print ("There are only", drivers, "drivers available.");
print ("There will be", cars_not_driven, "empty cars today.");
print ("We can transport", carpool_capacity, "people today.");
print ("We have", passengers, "to carpool today.");
print ("We need to put about", average_passengers_per_car, "in each car.");
print ("My apples:", my_1apples1);