class Car:
    name= ""
    color= ""
    def start():
        print("Starting the engine")


Car.name= 'Axio'
Car.color='Black'
print("name of the car: ", Car.name)
print('color: ', Car.color)

Car.start()