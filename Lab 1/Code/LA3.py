class Flight:
    def __init__(self, flight_number, airways):
        self.f_n=flight_number
        self.a=airways
    def display_flight(self):
        print("flight number is", self.f_n)
        print("airways is", self.a)
class Employee:
    def __init__(self, employee_id, employee_name, employee_gender):
        self.e_id=employee_id
        self.e_n=employee_name
        self.e_g=employee_gender
    def display_employee(self):
        (print("employee id is",self.e_id))
        (print ("employee name is", self.e_n))
        (print("employee gender is", self.e_g))
class Passenger:
    def __init__(self):
        Passenger.name=input("enter the name of passenger")
        Passenger.__passport=(input("enter the passport number"))
        Passenger.age=int(input("enter age of passenger"))
        Passenger.gender=input("enter the gender")
        Passenger.type=input("enter the type of class Business/Economy")
class Baggage:
    def __init__(self):
        Baggage.cabin=int(input("enter number of cabin"))
        Baggage.bag=int(input("enter number of main luggage"))
class Fare(Passenger,Baggage):                                                              #multiple inheritance
    def __init__(self):
        if (Passenger.type=="Business" or Passenger.type=='business'):
            Fare.fare=500
        elif(Passenger.type=="Economy" or Passenger.type=='economy'):
            Fare.fare=250
        else:
            print("please select appropriate class")


        if(Baggage.cabin>1):
            Fare.cabin_fare=(Baggage.cabin-1)*10
        else:
            Fare.cabin_fare=0
        if(Baggage.bag>2):
            Fare.bagg_fare=(Baggage.bag-2)*20
        else:
            Fare.bagg_fare=0
    def total_fare(self):
        t= Fare.fare+Fare.cabin_fare+Fare.bagg_fare
        print("your ticket is")
        (print("Fare of ticket is", t))
        (print("name of passenger", Passenger.name))
        (print("gender of passenger",Passenger.gender))

f1=Flight("7689","american airlines")
f1.display_flight()
e1=Employee("890","manu","female")
e1.display_employee()
p1=Passenger()
b1=Baggage()
f1=Fare()
f1.total_fare()

