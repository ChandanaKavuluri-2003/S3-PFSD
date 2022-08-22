class Reservation:
    def display(self,name,age):
        print("-----Passenger details-------")
        print("Name : ", name)
        print("Age : " , age)
class Ticket(Reservation):
            def displaytraindetails(self,tno,tname,seatno):
                print("******Reservation successful*****")
                print("------Train Details----------")
                print("Train number : ",tno)
                print("Train name : ",tname)
                print("Seat number : ",seatno)
count=0
while(True):
    ch=int(input("Click 1 for reservation"))
    if(ch==1):
        if(count<=3):
            t= Ticket()
            tnum=int(input("Enter the train number"))
            tname=input("Enter train name")
            seatno=int(input("Enter seat number"))
            pname=input("Enter passenger name")
            age=int(input("Enter passenger age"))
            t.displaytraindetails(tnum,tname,seatno)
            t.display(pname,age)
            count=count+1
        else:
            print("Sorry fully booked!!")
            break
    else:
        break





