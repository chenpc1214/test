class Father():
    
    def __init__(self):
        self.fathermoney = 10000
   
class Ira(Father):                                  
    
    def __init__(self):
        self.iramoney = 8000
        super().__init__()
    def get_money(self):                            
        print("Ira資產: ", self.iramoney,
              "\n父親資產: ", self.fathermoney,
              "\nIvan資產 : ", Ivan().ivanmoney)    
   
class Ivan(Father):                                 
    
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()   
    def get_money(self):                            
        print("Ivan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\nIra資產 : ", Ira().iramoney)       

ira = Ira()
ira.get_money()       



"""自己的寫法

class father():
    
    def __init__(self):
        self.fathermoney = 10000

class ivan(father):
    
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()

    def get_money(self):
        print("Ira的資產:",self.iramoney,
              "\n父親的資產:",self.fathermoney,
              "\nIvan的資產:",self.ivanmoney)
        
class ira(father):

    def __init__(self):
        self.iramoney = 8000
        super().__init__()

ira = ira()
ira.iramoney()
ira.get_money()"""
