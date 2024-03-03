class Bill:
    def __init__(self):
        self.money = 9
    def add(self, count):
        self.money += count
    def buy(self,count, name):
        pass

leo_bill = Bill()
print(leo_bill.money)

leo_bill.add(10)
leo_bill.add(20)

print(leo_bill.money)

kate_bill = Bill()
print(kate_bill.money)

kate_bill.add(1)
print(kate_bill.money)

print('А у Лео осталось 30 так как это другой объект', leo_bill.money)



class Person:
    def say_hello(self):
        print('Hello')

tom = Person()
tom.say_hello()



class Person:
    def say(self, message):
        print(message)
    def say_hello(self):
        print('Hello work')


tom = Person()
tom.say_hello()


class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def say1(self):
        print(self.name, self.color)


volga = Car('Волга', 'Серый')
uaz = Car('УАЗ', 'Зелёный')
volga.say1()
uaz.say1()







