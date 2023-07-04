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
# Create the first Fan object
# Create the second Fan object
# Display each object's properties