'''
class Employee:
    pass
# pass is a keyword which means nothing.
'''

'''
class Phone:  # class name starts with a capital letter
    def make_call(self):
        print('making a phone call')

    def play_game(self):
        print('Playing game')

    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost


p1 = Phone()  # object
p1.set_color('red')
p1.set_cost(10000)
col = p1.show_color()
rs = p1.show_cost()
print('color is :', col)
print('cost is :', rs)
p1.make_call()
p1.play_game()
'''


class Employee:
    def __init__(self, name, age, salary, gender):  # init method acts as a constructor
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print('Name of the Employee is :', self.name)
        print('Age of the Employee is :', self.age)
        print('Salary of the Employee is :', self.salary)
        print('Gender of the Employee is :', self.gender)


e1 = Employee('Satish', 20, 100000, 'Male')  # object e1
e1.employee_details()


'''Inheritance'''

# 1. Single Inheritance


class Vehicle:  # base class or super class
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print('i am a vehicle')
        print('Mileage of Vehicle is :', self.mileage)
        print('cost of Vehicle is :', self.cost)


v1 = Vehicle(1000, 55000)
v1.show_details()


class Car(Vehicle):  # child class
    def __init__(self, mileage, cost, tyres, hp):
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp = hp

    def show_car(self):
        print('I am a Car')
        print('Number of tyres are :', self.tyres)
        print('Value of horse power :', self.hp)


c1 = Car(200, 1200, 4, 224)
c1.show_details()
c1.show_car()


# 2. Multiple Inheritance
class Parent1:  # parent class 1
    def assing_string_one(self, str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1


class Parent2:  # parent class 2
    def assing_string_two(self, str2):  # setter
        self.str2 = str2

    def show_string_two(self):  # getter
        return self.str2


class Child(Parent1, Parent2):  # child class
    def assing_string_three(self, str3):
        self.str3 = str3

    def show_string_three(self):
        return self.str3


d1 = Child()  # object d1
d1.assing_string_one('i am string of parent 1')
d1.assing_string_two('i am string of parent 2')
d1.assing_string_three('i am string of child')
on = d1.show_string_one()
tw = d1.show_string_two()
th = d1.show_string_three()
print('string 1 :', on)
print('string 2 :', tw)
print('string 3 :', th)


# 3. Multilevel Inheritance
class Parent:
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name


class Child(Parent):
    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age


class GrandChild(Child):
    def assign_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender


gc = GrandChild()  # object
gc.assign_name('naveen')
gc.assign_age(21)
gc.assign_gender('Male')
name = gc.show_name()
age = gc.show_age()
gen = gc.show_gender()
print('Name :', name)
print('Age :', age)
print('Gender :', gen)
