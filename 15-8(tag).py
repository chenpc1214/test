
class Banks():
    
    title = 'Taipei Bank'                   
    def __init__(self, uname, money):       
        self.name = uname                   
        assert money >= 100, '開戶金額必需大於或等於100'
        self.balance = money
    def save_money(self, money):            
        assert money > 0, '存款money必需大於0'
        self.balance += money               
        print("存款 ", money, " 完成")      

    def withdraw_money(self, money):        
        assert money > 0, '提款money必需大於0'
        assert money <= self.balance, '存款金額不足'
        self.balance -= money               
        print("提款 ", money, " 完成")      

    def get_balance(self):                 
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               
hungbank.get_balance()                             
hungbank.save_money(300)                   
hungbank.get_balance()                      
chenbank = Banks('chen', -100)
chenbank.get_balance()                     




