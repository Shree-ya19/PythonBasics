#Basic oop concept

class Car:
    def __init__(self,model,color,speed):
        self.model=model
        self.color=color
        self.speed=speed

    def start_engine(self):
        print(f" {self.color} {self.model} is starting an engine")
    def drive(self):
        print(f" {self.color} {self.model}is travelling with {self.speed}")

bmw= Car(model="Sedan",color="Black", speed="12KM/HR")
bmw.start_engine()
bmw.drive()