'''
Design a class named Fan to represent a fan. The class contains:

Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
A private int data field named speed specifies the speed of the fan.
A private bool data field named on that specifies whether the fan is on (the default is False).
A private float data field named radius that specifies the radius of the fan.
A private string data field named color that specifies the color of the fan.
The accessor and mutator methods for all four data fields.
A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False). 
'''


class Fan:
    # Constants for fan speeds
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # Accessor methods
    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def is_on(self):
        return self.__on

    # Mutator methods
    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def turn_on(self):
        self.__on = True

    def turn_off(self):
        self.__on = False

    # String representation of the object
    def __str__(self):
        return ("Fan is " + ("on" if self.__on else "off") +
                ", Speed: " + str(self.__speed) +
                ", Radius: " + str(self.__radius) +
                ", Color: " + self.__color)



newFan = Fan()

print(newFan)