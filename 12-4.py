class banks():

    def __init__(self,uname):
        self.__name = uname
        self.__balance = 0
        self.__bankname = "fk"
        self.__rate = 30
        self.__service_change = 0.01

    def save_money(self,money):
        self.__balance += money
        print("存款",money,"完成")
        print("目前餘額",self.__balance,"元")

    def withdraw_money(self,money):
        self.__balance -= money
        print("提款",money,"完成")
        print("目前餘額",self.__balance,"元")

    def usd_change(self,usa_d):
        twd = int(usa_d * self.__rate * (1-self.__service_change))
        print("購買",usa_d,"美元")
        print("提款",twd,"完成")
        print(self.__name.title(),"目前餘額:",self.__balance - twd)

hung = banks("hung")
hung.save_money(5000)
hung.withdraw_money(3000)
hung.save_money(1500)
hung.usd_change(100)
