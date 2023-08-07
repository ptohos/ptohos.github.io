class Vehicle:
    def __init__(self,brand,model,type):
        self.brand = brand
        self.model = model
        self.type = type
        self.tank = 50
        self.fuel = 0

    def __str__(self):
        return f'This is {self.brand} car model {self.model} type {self.type}' 

    def fuel_up(self):
        self.fuel = self.tank
        print("Gas tank is full")

    def drive(self):
        print(f'The {self.model} is now driving')

    def update_fuel_level(self, new_level):
        if new_level <= self.tank:
            self.fuel = new_level
        else:
            print('Exceed capacity')

    def get_gas(self, amount):
        if (self.fuel + amount <= self.tank):
            self.fuel += amount
            print('Added fuel')
        else:
            print('The tank wont hold this amount of gas.')

    def test():
        car = Vehicle('Honda','Civic', 'Hatchback')
        print(car)
        car.update_fuel_level(30)
        car.fuel
        car.get_gas(15)
        car.fuel
#You can run it with Vehicle.test()
