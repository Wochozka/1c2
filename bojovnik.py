#!/usr/bin/env python3

import kostka

class Bojovnik:
    """
    Trida preprezentujici bojovnika do areny.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = kostka
    
    def __str__(self):
        return f"Bojovnik jmenem {self.__jmeno}."



if __name__ == "__main__":
    k = kostka.Kostka(10)
    b = Bojovnik("Adam", 100, 50, 80, k)
    c = Bojovnik("Eva", 150, 40, 60, k)
    print(b)
    print(c)
