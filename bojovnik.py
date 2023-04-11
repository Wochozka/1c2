#!/usr/bin/env python3

import kostka

class Bojovnik:
    """
    Trida preprezentujici bojovnika do areny.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__max_zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = kostka
        self.sprcha = 10
    
    def __str__(self):
        return f"Bojovnik jmenem {self.__jmeno}."

    @property
    def nazivu(self):
        return self.__zivot > 0
    
    def graficky_zivot(self):
        celkem = 20
        pocet = int(self.__zivot / self.__max_zivot * celkem)
        return f"[{'#'*pocet}{' '*(celkem-pocet)}]"

    def utok(self, souper):
        uder = self.__utok + self.__kostka.hod()
        print(f"{self} utoci na {souper} silou {uder}")
        souper.obrana(uder)

    def obrana(self, uder):
        obrana = self.__obrana + self.__kostka.hod()
        print(f"{self} se brani uderu {uder} obranou {obrana}")
        zraneni = uder - obrana
        print(f"{self} ma zraneni {zraneni}")
        if zraneni > 0:
            self.__zivot = self.__zivot - zraneni
        else:
            print(f"{self} odrazil utok.")

if __name__ == "__main__":
    k = kostka.Kostka(50)
    b = Bojovnik("Adam", 100, 80, 80, k)
    c = Bojovnik("Eva", 150, 40, 60, k)
    print(c.graficky_zivot())    
    b.utok(c)
    print(c.graficky_zivot())
