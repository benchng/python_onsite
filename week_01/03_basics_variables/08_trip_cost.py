'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

def total_cost():
    distance = float(input('miles to drive : '))
    mpg = float(input('MPG of the car (23.6 mpg is average) : '))
    fuel_price = float(input('Price per gallon of fuel (ranging around 2.3 - 3.5) : '))
    cost_of_trip = distance / mpg * fuel_price
    print(cost_of_trip)
    #print(f'The total cost of the trip is {cost_of_trip}')

total_cost()