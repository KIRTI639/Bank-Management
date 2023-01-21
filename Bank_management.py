from datetime import *
import os
import sys
from datetime import *

class Bank():
    def __init__(self):
        if os.path.exists("Bank.txt"):
            self.b = self.read()
        else:
            self.b = 0

    def deposit(self):
                
        amt = int(input("\t\tEnter Amount : "))
        #dt = datetime.today().date()
        self.b = self.b + amt

    def withdraw(self):
        a = int(input("\t\tEnter Amount : "))
        self.b = self.b - a

    def balance(self):
        print("\n\t\tCurrent Balance is : {}".format(self.b))

    def write(self):
        f = open("Bank.txt","a")
        #d = datetime.today().date()
        s = str(self.b)
        f.write(s)
        f.write("\n")
        f.close()

    def read(self):
        with open("Bank.txt") as f:
            d=f.readlines()
        return int(d[-1])

    
    def screen_2(self):
        print("\n\n\t\t1: Deposit Money")
        print("\t\t2: Withdraw Money")
        print("\t\t3: Check Balance")
        #print("4: Logout")
        print("\t\t4: Exit")
        c = int(input("\t\tEnter your choice : "))
        return c
    
    def screen_1(self):
        print("\n\n\t\t1: Create New Account")
        print("\t\t2: Login with Password")
        print("\t\t3: Exit")
        m = int(input("\t\tEnter your choice : "))
        return m

    def write_1(self,s):
        f = open("Login.txt","a")
        f.write(s)
        f.write("\n")
        f.close()
        
    def create(self):
        
        name = input("\t\tYour name : ")
        mob = input("\t\tMobile No : ")
        email  = input("\t\tEmail ID : ")
        pw = input("\t\tCreate Password : ")
        
        s = email+","+pw+','+name+","+mob
        self.write_1(s)
    def read_1(self):
        data={}
        with open("Login.txt") as f:
            d = f.readlines()
      #  print(d)
        for i in d:
            
            i=i.split(',')
            data[i[0]]=i[1]
            
        return data
        
    def login(self):
        id = input("\t\tEnter Email ID : ")
        pw = input("\t\tEnter paasword : ")
        data=self.read_1()
        if id in data:
            if pw == data[id]:
                return True
        else:
            print("\t\tUsername not found.")

## Bank Object
obj = Bank()

while True:
    m=obj.screen_1()
    if m==1:
        obj.create()
    elif m==2:
        r=obj.login()
        if r==True:
            #print("You are logged in")
            while True:
                c=obj.screen_2()
                if c==1:
                    obj.deposit()
                elif c==2:
                    obj.withdraw()
                elif c==3:
                    obj.balance()
                elif c==4:
                    obj.write()
                    sys.exit()
                        
                else:
                    print("\t\tPlease Enter Valid Number...!")

    elif m==3:
        sys.exit()
    else:
        print("\t\tPlease input valid number.")
        
