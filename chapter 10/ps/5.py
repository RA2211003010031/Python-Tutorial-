class Train:
    name = ""
    age = ""
    number = ""
    
    def setDetails(self):
        self.name = input("Enter your name : ")
        self.age = input("Enter your age: ")
        self.number = input("Enter your number: ")

    # method to book a ticket
    def bookTicket(self,trainNo,fro,to):
        print(f"Dear {self.name}\nYour Train Ticket has been successfully booked\n\tTrain No : {trainNo}\n\tFrom : {fro}\n\tTo : {to}")
        
    # get status(no of seats)
    def getStatus(self, trainNo):
        print(f"Dear\nTrain Number : {trainNo},\nSEATS:\t3AC = 40 | 2AC = 30")
    
    # get fare information of train running
    def getfare(self, trainNo, fro, to):
        print(f"The fare for Train No {trainNo} from {fro} to {to} is \n3AC = 1000 | 2AC = 2000")
    
    
p1 = Train()
p1.setDetails()
p1.bookTicket(12124,"Delhi","NJP")
p1.getStatus(12121)
p1.getfare(12121,"Delhi","NJP")