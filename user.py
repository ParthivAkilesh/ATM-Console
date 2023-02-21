from admin import ADMIN
ad = ADMIN()

class USER():
    
    def __init__(self):

        self.acc = {
            123:{"name":"Naruto" ,"balance":3000, "pin":1234},
            456:{"name":"Minato" ,"balance":7000, "pin":4567},
            789:{"name":"Luffy" ,"balance":4000, "pin":7890}
                   }
        
    def checkBalance(self):
            
            print(f"Your bank account has a balance of Rupees {self.acc[self.userAccNum]['balance']}/-")
    
    
    # def withdraw(self):
    #     a = int(input("Enter amount to withdraw: "))
    #     if (self.acc[self.userAccNum]["balance"] < a):
    #         print("INSUFFICIENT BALANCE\nEnter valid amount!")
    #         self.withdraw()
    #         return
    #     else:
    #         self.acc[self.userAccNum]["balance"] -= a
    #         self.miniStat()
    #         return
    
    def getDenom(self, amt):
        
        tempAmt = amt
        res = [0, 0, 0, 0]
        print("amout needed: ",amt)
        while(amt>0):
            # print("amt: ", amt)
            
            if amt >= 2000:
                temp = amt // 2000
                noteAvail = ad.checkDenom(temp, 2000)
                res[0] = noteAvail
                # print("amt before: ", amt, (noteAvail))
                amt -= (int(noteAvail) * 2000)
                print("amt: @2000: ", amt)
                
            elif amt >= 500:
                temp = amt // 500
                noteAvail = ad.checkDenom(temp, 500)
                res[1] = noteAvail
                amt = amt - (int(noteAvail) * 500)
                print("amt: @500 : ", amt)
                
            elif amt >= 200:
                temp = amt // 200
                noteAvail = ad.checkDenom(temp, 200)
                res[2] = noteAvail
                amt = amt - (int(noteAvail) * 200)
                print("amt: @200: ", amt)
                
            elif amt >= 100:
                temp = amt // 100
                noteAvail = ad.checkDenom(temp, 100)
                res[3] = noteAvail
                amt = amt - (int(noteAvail) * 100)
                print("amt: @100: ", amt)
                
            else:
                print("SORRY! CANNOT LOAD MONEY WITH AVAILABLE DENOMINATION")
                break
        self.acc[self.userAccNum]['balance'] -= tempAmt   
        print("printing denom.......................")
        ad.getDenom()
        print("over----------------------------------") 
        return res
    
    def withdraw(self):
        
        amt = int(input("Enter amount to withdraw: "))
        denom = [2000, 500, 200, 100]
        if self.acc[self.userAccNum]['balance'] >= amt:
            # ad = ADMIN()
            if ad.balance() >= amt:
                resDenom = self.getDenom(amt)
                print("************WITHDRWING MONEY************")
                for i in range(len(resDenom)):
                    print(f"The denomination for {denom[i]} = {int(resDenom[i])}")
                print("****************ThankYou****************")
            else:
                print("SORRY FOR THE INCOVENIENCE, INSUFFICIENT BALANCE AT ATM DECK")
                return
        else:
            print("INSUFFICIENT BALANCE!")
            return
    
    def miniStat(self):
        
        print("Naruto Shippuden Bank Private Limited")
        print("*************************************")
        print(" ")
        print(f"Account Number : {self.userAccNum}")
        print(f"Account Name : {self.acc[self.userAccNum]['name']}")
        print(f"Account Balance : {self.acc[self.userAccNum]['balance']}")
        print("*************************************")
        print("Thank You! See you again!")
        print("*************************************")
    
    
    
    def deposit(self):
        
        # ad = ADMIN()
        ad.loadAmt()
        return
        
    def moneyTrans(self):
        
        recAcc = int(input("Enter the account number to make the transfer: "))
        transAmt = int(input("Enter the amount to be transferred: "))
        if transAmt < self.acc[self.userAccNum]["balance"]:
            try:
                self.acc[recAcc]["balance"]+=transAmt
                self.acc[self.userAccNum]["balance"]-=transAmt
                print(f"Amount successfully transferred to {self.acc[recAcc]['name']}!")
                self.miniStat()
            except:
                print("ACCOUNT INVALID OR UNAVAILABLE")
        else:
            print("TRANSACTION INVALID")
            self.moneyTrans()
            
        return             
            
    def pinChange(self):
        
        cpin = int(input("Enter your current PIN: "))
        if cpin == self.acc[self.userAccNum]['pin']:
            npin = int(input("Enter new PIN: "))
            self.acc[self.userAccNum]['pin'] = npin
            print("PIN changed successfully")
        else:
            print("INVALID PIN")
            self.pinChange()
            
        return
             
    
    def options(self):
        ch = int(input("1.Check Balance\n2.Withdraw Money\n3.Mini Statement\n4.Deposit Money\n5.Transfer Money\n6.Change PIN\nEnter your choice: "))
        while(ch<7):
            if ch == 1:
                self.checkBalance()
            elif ch == 2:
                self.withdraw()
            elif ch == 3:
                self.miniStat()
            elif ch == 4:
                self.deposit()
            elif ch == 5:
                self.moneyTrans()
            elif ch == 6:
                self.pinChange()
            ch = int(input("1.Check Balance\n2.Withdraw Money\n3.Mini Statement\n4.Deposit Money\n5.Transfer Money\n6.Change PIN\nEnter your choice: "))    
            
        return
        
    def login(self):
        
        self.userName = input("Enter your name: ")
        self.userAccNum = int(input("Enter your account number: "))
        if self.acc[self.userAccNum]["name"] == self.userName:
            print(f"<<LOGGED IN AS {self.userName}>>")
            self.options()
            print("LOGGING OUT")
            return
            
            
        # return