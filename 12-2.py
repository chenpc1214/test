class myschool():
    
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def msg(self):
        print("Hi!", self.name.title(),"你的成績是", self.score,"分")


hung = myschool("kevin",80)
hung.msg()
