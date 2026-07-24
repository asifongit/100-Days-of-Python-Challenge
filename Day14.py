# Given a string s representing time in 24-hour format "HH:MM", compute the smallest angle in degrees between the hour and minute hands of an analog clock.

def get_angle(string):

    # first we need to split the minuts and hour
    split=string.split(":")

    # convert string to integer    
    hour =int(split[0])
    minuts =int(split[1])

    hour = hour % 12

    minut_angle= minuts*6

    base_position_hour=hour*30

    hour_angle=minuts*0.5+base_position_hour

    difference=abs(minut_angle-hour_angle)


    smallest_angle = min(difference, 360 - difference)

    print(f"Smallest angle is: : {smallest_angle}")






get_angle("6:00")
