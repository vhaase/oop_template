# Meine Vorlage zum ausprobieren

class Addieren:
    def __init__(self):
        self.Sum1 = None
        self.Sum2 = None
        self.Summe = None

    def addiere(self, sum1, sum2):
        self.Sum1 = sum1
        self.Sum2 = sum2
        self.Summe = self.Sum1 + self.Sum2
        return self.Summe


class Subtrahieren:
    def __init__(self):
        self.Subtr1 = None
        self.Subtr2 = None
        self.Subtr = None

    def subtrahiere(self, subtr1, subtr2):
        self.Subtr1 = subtr1
        self.Subtr2 = subtr2
        self.Subtr = self.Subtr2 - self.Subtr1
        return self.Subtr
class Rechner(Addieren, Subtrahieren):
    def __init__(self):
        self.Multi = None

    def multi(self, sum1, sum2, subtr1, subtr2):
        self.Sum1 = sum1
        self.Sum2 = sum2
        self.Subtr1 = subtr1
        self.Subtr2 = subtr2
        self.Multi = self.addiere(self.Sum1, self.Sum2) * self.subtrahiere(self.Subtr1, self.Subtr2)
        return self.Multi


# hier geht's los
if __name__ == '__main__':
    add = Addieren()
    diff = Subtrahieren()

    print("Addition, Summe: ", add.addiere(23, 45))

    print("\nSubtraktion, Differenz", diff.subtrahiere(15, 56))

    calc = Rechner()

    A = calc.addiere(34, 23) * calc.subtrahiere(11, 34)

    print("\nmulti ohne methode:", A)

    print("\nmulti mit methode: ", calc.multi(1,2,3,4))

    print("\nfertig")

    print("====================================================================")
