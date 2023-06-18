# Meine Vorlage zum ausprobieren

import Konstante
import sharepoint
import Funktionen


# hier geht's los
if __name__ == '__main__':
    add = Funktionen.Addieren()
    diff = Funktionen.Subtrahieren()

    print("Addition, Summe: ", add.addiere(Konstante.Summand1, Konstante.Summand2))

    print("\nSubtraktion, Differenz", diff.subtrahiere(15, 56))

    calc = Funktionen.Rechner()

    A = calc.addiere(34, 23) * calc.subtrahiere(11, 34)

    print("\nmulti ohne methode:", A)

    print("\nmulti mit methode: ", calc.multi(1, 2, 3, 4))

    print("\nfertig")

    SP=sharepoint.SharePoint()
    SP.accessFolders()
