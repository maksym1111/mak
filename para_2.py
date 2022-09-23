import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progres = 0
        self.food = 100
        self.water = 100
        self.money = random.randint(1000, 5000)
        self.alive = True
    def to_studi(self):
        print("time to study")
        self.progres += 0.12
        self.gladness -= 3
        self.food -= 20
        self.water -= 20
    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3
        self.food -= 10
    def to_chill(self):
        print("time to chill")
        self.gladness += 5
        self.money -= 0
    def to_eat(self):
        print("time to food")
        self.money -= 50
        self.food += 60
    def to_drink(self):
        print("time to drink")
        self.water += 30
        self.money -= 50
    def to_job(self):
        print("time to work")
        self.gladness -= 10
        self.water -= 20
        self.food -= 20
        self.money += 1000
    def is_alive(self):
        if self.progres < -0.5:
            print('Cast out')
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progres > 5:
            print("Done!")
            self.alive = False
        elif self.food <= 0:
            print("You dead")
            self.alive = False
        elif self.water <= 0:
            print("You dead")
            self.alive = False
        elif self.money <= 0:
            print("You are bankrupt")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progres = {round(self.progres , 2)}")
        print(f"food = {self.food}")
        print(f"Water = {self.water}")
        print(f"money = {self.money}")
    def live(self, day):
        day = "Day" + str(day) +"of" + self.name +"life"
        print(f"{day:=^50}")
        life_cube = input("1-sleep 2-studi\n3-eat 4-chill\n5-drink 6-work\n");
        if life_cube == "1":
            self.to_studi()
        elif life_cube == "2":
            self.to_sleep()
        elif life_cube == '3':
            self.to_chill()
        elif life_cube == '4':
            self.to_eat()
        elif life_cube == '5':
            self.to_drink()
        elif life_cube == '6':
            self.to_job()
        self.end_of_day()
        self.is_alive()
name = Student(name= input("Enter your name "))
for day in range(365):
    if name.alive == False:
        break
    name.live(day)



