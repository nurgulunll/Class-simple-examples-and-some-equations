#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#q1
class ContestResult():
    def __init__(self,winner="",second_place="",third_place=""):
        self.winner=winner
        self.second_place=second_place
        self.third_place=third_place
        
    def set_winner(self,winner):
        self.winner=winner
    def set_second_place(self,second_place):
        self.second_place=second_place     
    def set_third_place(self,third_place):
        self.third_place=third_place
        
    def get_winner(self):
        return self.winner
    def get_second_place(self):
        return self.second_place
    def get_third_place(self):
        return self.third_place
    
#q2
class WeatherForecast():
     def __init__(self,skies=" ",high=0,low=0):

def set_skies(self, skies):
    self.skies = skies

def get_skies(self):
    return self.skies

def set_high(self, high):
    self.high = high

def get_high(self):
    return self.high

def set_low(self, low):
    self.low = low

def get_low(self):
    return self.low

#question3
class Quadrilateral():
    def __init__(self,x,y,x1,y1,x2,y2,x3,y3):
        self.x = x
        self.x1 =x1
        self.x2 = x2
        self.x3 = x3

        self.y = y
        self.y1 =y1
        self.y2 =y2
        self.y3 =y3
        
    def coordinates(self):
        return (f"A({self.x},{self.y}) B({self.x1},{self.y1}) C({self.x2},{self.y2}) D({self.x3},{self.y3})" )
                
def main():
    print("Coordinates of Quadrilateral are :")
    k = Quadrilateral(1,2,3,4,5,6,7,8)
    print(k.coordinates())
        
main()
print()
class Trapezoid(Quadrilateral):
    def __init__(self,x=0,y=0,x1=10,y1=0,x2=8,y2=5,x3=3.3,y3=5):
        super().__init__(x,y,x1,y1,x2,y2,x3,y3)
        
    def Coordinates(self):
        return (f"A({self.x},{self.y}) B({self.x1},{self.y1}) C({self.x2},{self.y2}) D({self.x3},{self.y3})" )
        
    def Height(self):
        return (f"Height is = {self.y3}")
    def Area(self):
        return ("Area = 36.75")
    
def main1():
    print("Coordinates of Trapezoid are :")
    m = Trapezoid()
    print(m.coordinates())
    print(m.Height())
    print(m.Area())
    
    
main1()
print()

class Parallelogram(Quadrilateral):
    def __init__(self,x=5,y=5,x1=11,y1=5,x2=12,y2=20,x3=6,y3=20):
        super().__init__(x,y,x1,y1,x2,y2,x3,y3)
        
    def Coordinates2(self):
        return (f"A({self.x},{self.y}) B({self.x1},{self.y1}) C({self.x2},{self.y2}) D({self.x3},{self.y3})" )
    
    def Width(self):
        return ("Width = 6")
    
    def Height2(self):
        return ("Height = 15")
    
    def Area2(self):
        return ("Area = 90")
        
def main2():
    print("Coordinates of Parallelogram  are :")
    s = Parallelogram()
    print(s.Coordinates2())
    print(s.Width())
    print(s.Height2())
    print(s.Area2())
    
main2() 
print()   
    
class Rectangle(Quadrilateral):
    def __init__(self,x=17,y=14,x1=30,y1=14,x2=30,y2=28,x3=17,y3=28):
        super().__init__(x,y,x1,y1,x2,y2,x3,y3)
        
    def Coordinates3(self):
        return (f"A({self.x},{self.y}) B({self.x1},{self.y1}) C({self.x2},{self.y2}) D({self.x3},{self.y3})" )
        
        
    def Width1(self):
        return ("Width = 13")
    
    def Height3(self):
        return ("Height = 14")
    
    def Area3(self):
        return("Area = 182")
    
        
def main3():
    print("Coordinates of Rectangle are :")
    e = Rectangle()
    print(e.Coordinates3())
    print(e.Width1())
    print(e.Height3())
    print(e.Area3())
    

main3()
print()
    
class Square(Quadrilateral):
    def __init__(self,x=4,y=0,x1=8,y1=0,x2=8,y2=4,x3=4,y3=4):
        super().__init__(x,y,x1,y1,x2,y2,x3,y3)
        
    def Coordinates4(self):
        return (f"A({self.x},{self.y}) B({self.x1},{self.y1}) C({self.x2},{self.y2}) D({self.x3},{self.y3})" )
        
    def Sides(self):
        return ("Sides are = 4 ")
    
    def Area4(self):
        return ("Area = 16 ")
    
def main4():
    print("Coordinates of Square are :")
    d = Square()
    print(d.Coordinates4())
    print(d.Sides())
    print(d.Area4())
    
main4()

#question4
class Employee():
    def __init__(self,first_name,last_name,month="May"):
        self.first_name = first_name
        self.last_name = last_name
        self.month = month        
    def __str__(self):
        return "%s %s" % (self.first_name,self.last_name)
    def _checkPositive(self,value):
        self.value = value
        if self.value < 0 :
            return "plz give a pozitive value"
        else:
            return self.value
    def DepartmentCode(self):
        return 1
    

class Boss(Employee):
    def __init__(self, first_name, last_name,salary,birthDate0):
        super().__init__(first_name, last_name)
        self.salary=self._checkPositive(float(salary))
        self.birthDate0=birthDate0
    def earnings(self):
        return self.salary
    def __str__(self):
        return "%17s: %s" % ("Boss",Employee.__str__(self))
    def birthDate(self):
        return self.birthDate0 
    def Bonus(self):
        if self.month == self.birthDate0 :
            return self.salary +100
        else:
            return self.salary
        
class HourlyWorker(Employee):
    def __init__(self, first_name, last_name,wage,hours,birthDate1):
        super().__init__(first_name, last_name)
        self.wage = self._checkPositive(float(wage))
        self.hours = self._checkPositive(float(hours))
        self.birthDate1 = birthDate1
    def earnings(self):
        if self.hours <= 40 :
            return self.wage * self.hours
        else:
            return 40 * self.wage + (self.hours-40) * (self.wage * 1.5)
    def __str__(self):
        return "%17s: %s" % ("HourlyWorker",Employee.__str__(self))
    def birthDate(self):
        return self.birthDate1
    def Bonus(self):
        if self.month == self.birthDate1:
            return (40 * self.wage + (self.hours-40) * (self.wage * 1.5)) + 100
        else:
            return (40 * self.wage + (self.hours-40) * (self.wage * 1.5))        
    
class PieceWorker(Employee):
    def __init__(self, first_name, last_name,wage,quantity,birthDate2):
        super().__init__(first_name, last_name)
        self.wagePerPiece = self._checkPositive(float(wage))
        self.quantity = self._checkPositive(quantity)
        self.birthDate2 = birthDate2     
    def earnings(self):
        return self.quantity * self.wagePerPiece
    def __str__(self):
        return "%17s: %s" % ("PieceWorker",Employee.__str__(self))
    def birthDate(self):
        return self.birthDate2
    def Bonus(self):
        if self.month == self.birthDate2 :
            return self.quantity * self.wagePerPiece + 100
        else:
            return self.quantity * self.wagePerPiece

        
class CommisionWorker(Employee):
    def __init__(self,first_name,last_name,salary,commision,quantity,birthdate3):
        super().__init__(first_name,last_name)
        self.salary=self._checkPositive(float(salary))
        self.commision=self._checkPositive(float(commision))
        self.quantity=self._checkPositive(quantity)
        self.birthdate3=birthdate3       
    def earnings(self):
        return self.commision+self.salary*self.quantity
    def __str__(self):
        return "%17s: %s" % ("CommisionWorker",Employee.__str__(self))
    def birthDate(self):
        return self.birthdate3
    def Bonus(self):
        if self.month == self.birthdate3 :
            return self.commision+self.salary*self.quantity + 100
        else:
            return self.commision+self.salary*self.quantity
        
        
class Date(Employee):
    def __init__(self,first_name,last_name,day,month,year):

        super().__init__(first_name, last_name)
        self.year = year
        self.day = day
    def birthDate(self):
        return self.day / self.month / self.year

        
    


employees = [Boss("John","Smith",800.00,"September"),
             CommisionWorker("Sue", "Jones", 200.0, 3.0, 150,"May"),
             PieceWorker("Bob", "Lewis", 2.5, 200,"November"),
             HourlyWorker("Karen","Price", 13.75, 40,"May")]
for employee in employees:
    print("%s earned $%.2f" % (employee,employee.earnings()))
    

employees = [Boss("John","Smith",800.00,"September"),
             CommisionWorker("Sue", "Jones", 200.0, 3.0, 150,"May"),
             PieceWorker("Bob", "Lewis", 2.5, 200,"November"),
             HourlyWorker("Karen","Price", 13.75, 40,"May")]
for employee in employees:
    print(employee," " +"Birthday Month =" ,employee.birthDate())

print("May=> 100 dollars bonus will add ur salary")

for k in employees:
    print(k.__str__(),"earned",k.Bonus())

