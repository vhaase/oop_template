


import Konstante
import sharepoint


class Addieren:
    def __init__(self):
        self.Sum1 = None
        self.Sum2 = None
        self.Summe = None

    def addiere(self, sum1, sum2):
        self.Sum1 = sum1
        self.Sum2 = sum2

        return self.Sum1 + self.Sum2


class Subtrahieren:
    def __init__(self):
        self.Subtr1 = None
        self.Subtr2 = None
        self.Subtr = None

    def subtrahiere(self, subtr1, subtr2):
        self.Subtr1 = subtr1
        self.Subtr2 = subtr2

        return self.Subtr2 - self.Subtr1


class Rechner(Addieren, Subtrahieren):
    def __init__(self):
        """
        Diese Klasse erbt von Addieren und Subtrahieren. Ausserdem wird eine zusätzliche Methode eingeführt, die
        mehrere berechnen kombiniert.
        """
        super().__init__()
        self.Multi = None

    def multi(self, sum1, sum2, subtr1, subtr2):
        self.Sum1 = sum1
        self.Sum2 = sum2
        self.Subtr1 = subtr1
        self.Subtr2 = subtr2

        return self.addiere(self.Sum1, self.Sum2) * self.subtrahiere(self.Subtr1, self.Subtr2)
