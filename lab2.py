# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height2(h0, t):
    g=9.81
    result= h0-1/2*g*t**2
    return result
h0=float(input("Enter initial height (meters): "))
t=float(input("Enter time (s): "))
print("The height of the ball at", t, " seconds is",(calculate_height2(h0,t)), " meters.")

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(time):
    result= 20*t
    return result
time=float(input("Enter time for car (in seconds):"))
print("The car will travel", calculate_car_distance(time), " meters in", time, " second(s)")