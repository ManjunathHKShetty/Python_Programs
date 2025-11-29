class Animals:
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.mammals = True
        self.tail = True

    def isMammal(self):
        if self.mammals:
            print("It is mammal.")

    def isDomestic(self):
        if self.domestic:
            print("It is a Domestic animal.")


class Dogs(Animals):
    def __init__(self):
        super().__init__()

    def isMammal(self):
        super().isMammal()
        super().isDomestic()


class Horses(Animals):
    def __init__(self):
        super().__init__()

    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail.")


Tom = Dogs()
Tom.isMammal()
Jack = Horses()
Jack.hasTailandLegs()
