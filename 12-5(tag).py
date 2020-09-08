class Banks():

    def __init__(self, uname):              
        self.__name = uname                 
        self.__balance = 0                  
        self.__bankname = "Taipei Bank"     
        self.__rate = 30                
        self.__service_charge = 0.01        

    def save_money(self, money):            
        self.__balance += money             
        print("存款 ", money, " 完成")      

    def withdraw_money(self, money):        
        self.__balance -= money             
        print("提款 ", money, " 完成")      

    def get_balance(self):                  
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   
        return self.__bankname

class Shilin_Banks(Banks):
    ''' 定義士林分行'''
    def __init__(self, uname):
        self.bankname = "Taipei Bank - Shilin Branch"  
    def bank_title(self):                   
        return self.bankname

class Beitou_Banks(Banks):
    ''' 定義北投分行'''
    def __init__(self, uname):
        self.bankname = "Taipei Bank - Beitou Branch"
    def bank_title(self):                   
        return self.bankname

jamesbank = Banks('James')                  
print("James's banks = ", jamesbank.bank_title())  
hungbank = Shilin_Banks('Hung')             
print("Hung's banks  = ", hungbank.bank_title())   
kevinbank = Shilin_Banks('Kevin')           
print("Kevin's banks = ", kevinbank.bank_title())  



"""自己做的

class bank():
    
    def something(self):
        bank_name = "taipei bank"
        print("James's banks = ",bank_name.title())

class shilin(bank):
    
    def something(self):
        bank_name = "taipei bank - shilin bank"
        print("Hung's banks =",bank_name.title())

class beitou(bank):
    
    def something(self):
        bank_name = "taipei bank - shilin bank"
        print("Kevin's banks =",bank_name.title())

a = bank()
a.something()
a.shilin()
a.beitou()
"""
