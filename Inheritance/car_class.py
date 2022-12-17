class Car(Vehicle):
    """Car class"""
    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, "is changing gear to", gear_name)
        