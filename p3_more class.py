class Human :
    def __init__(self,name = "Human"):
        self.name =name


class Auto:
     def __init__(self,brand):
         self.brand = brand
         self.passenger = []
      def add_passenger(self,human):
          self.passenger.appenger(human)


      def print_passenger(self):
          if self.passenger! = []:
              print(f"Names  of {self.brend} passenger")
              for passenger in self.passenger:
                 print(passenger.name)
          else:
              print(f"There are no passenger {self.brand}")


judi =  Human("Judi")
person2 = Human("Jack")
car1 = Auto ("Tayota")
car2 = Auto ("Audi")

car1.print_passenger()
car2.print_passenger()

car1.add_passenger("Judi")
car2.add_passenger()

car1.print_passenger()
car2.print_passenger()



