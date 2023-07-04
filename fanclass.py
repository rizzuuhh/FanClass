# Define the Fan class with the specified attributes
class Fan:
    def __init__(self):
        self.__speed = "SLOW"
        self.__radius = 5
        self.__color = "blue"
        self.__on = False
# Setter methods
    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_on(self, on):
        self.__on = on

# Getter methods
    def get_speed(self):
        return self.__speed
    
    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_on(self):
        return self.__on

# Create the first Fan object
fan1 = Fan()
fan1.set_speed("MAXIMUM")
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)

# Create the second Fan object
# Display each object's properties