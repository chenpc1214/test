class grandfather():

    def __init__(self):
        super().__init__()
        self.grandfathermoney = 10000
    def get_information(self):
        print("grandfather's information")

class grandmother():

    def __init__(self):
        super().__init__()
        self.grandmothermoney = 20000
    def get_information3(self):
        print("grandmother's information")

class father(grandfather,grandmother):

    def __init__(self):
        super().__init__()
        self.fathermoney = 8000
    def get_information2(self):
        print("father's information")

class ivan(father):

    def __init__(self):
        super().__init__()
        self.ivanmoney = 3000
    def get_information4(self):
        print("ivan's information")

    def get_money(self):
        print("\nIvan的資產:",self.ivanmoney,
              "\n父親的資產:",self.fathermoney,
              "\n爺爺的資產:",self.grandfathermoney,
              "\n奶奶的資產:",self.grandmothermoney,)

ivan = ivan()
ivan.get_information4()
ivan.get_information2()
ivan.get_information()
ivan.get_information3()
ivan.get_money()
