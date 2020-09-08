class grandfather():

    def action(self):
        print("grandfather")
        
class father(grandfather):

    def action2(self):
        print("father")

class uncle(grandfather):

    def action2(self):
        print("uncle")
        

class aunt(grandfather):

    def action2(self):
        print("aunt")


class ivan(uncle,aunt,father):

    def action3(self):
        print("ivan")

a = ivan()
a.action3()
a.action2()
a.action()

