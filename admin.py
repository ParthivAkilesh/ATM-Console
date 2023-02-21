class ADMIN():
    
    def __init__(self):
        self.admin_name = "Admin"
        self.admin_pass = "admin"
        self.balDem = {2000:5, 500:5, 200:2, 100:5}
        self.bal = sum([i*self.balDem[i] for i in self.balDem])
        
        
    def SubLoadAmt(self, amt):
        
        notes = int(input(f"Number of Notes for {amt}: "))
        if self.balDem[amt]+notes <= 5:
                self.balDem[amt]+=notes
                self.bal+=(notes*amt)
                return
        else:
                print("cannot load the money reached more than full capacity")
                print("RETRY AGAIN ")
                self.SubLoadAmt(amt)
                return 
                
        
    def balance(self):
        return self.bal
        
    def loadAmt(self):
        if self.bal == 14000:
            print("ATM has been loaded full capacity")
            return ""
        else:
            print("Enter amount by denomination: ")
            self.SubLoadAmt(2000)
            self.SubLoadAmt(500)
            self.SubLoadAmt(200)
            self.SubLoadAmt(100)
            self.checkBalance()
            print("Loaded Successfully!!")
            return
            
    def checkBalance(self):
        total = 0
        print("Checking Balance::")
        for i in self.balDem:
            print(f"Number of notes for {i}: {self.balDem[i]} | Current total: {total + self.balDem[i]*i}")
            total+=self.balDem[i]*i            
        return
            
    def checkDenom(self, note, amot):         
         if self.balDem[amot] >= note:            
             self.balDem[amot] -= note
             return note         
         else:
             return self.balDem[amot]
     
    def getDenom(self):
         
         print(self.balDem)
         return
         
    def options(self):
        print("You are logged in as Admin")
        ch = int(input("1.Load Money\n2.Check ATM Balance\n3.EXIT\nEnter your choice: "))
        while(ch<3):
            if ch == 1:
                self.loadAmt()
            elif ch == 2:
                self.checkBalance()
            ch = int(input("1.Load Money\n2.Check ATM Balance\n3.EXIT\nEnter your choice: "))    
            
        return
     
    def login(self):
        adminName = input("Enter your name: ")
        adminPass = input("Enter Password: ")
        if (adminName == self.admin_name) and (adminPass == self.admin_pass):
            self.options()
            print("LOGGING OUT")
            return 
        