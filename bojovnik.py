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
        self._zprava = ""
    
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
        self._zprava = f"{self.__jmeno} utoci na {souper.__jmeno} silou {uder}."
        souper.obrana(uder)

    def obrana(self, uder):
        obrana = self.__obrana + self.__kostka.hod()
        zraneni = uder - obrana
        if zraneni > 0:
            self._zprava = f"{self.__jmeno} utrpel zraneni o sile {zraneni}."
            self.__zivot = self.__zivot - zraneni
            if self.__zivot <= 0:
                self.__zivot = 0
                self._zprava = self._zprava[:-1] + " a zemrel."
        else:
            self._zprava = f"{self.__jmeno} zcela odrazil utok."
    
    def setZprava(self, zprava):
        self._zprava = zprava
    
    def getZprava(self):
        return self._zprava

if __name__ == "__main__":
    k = kostka.Kostka(50)
    adam = Bojovnik("Adam", 100, 80, 80, k)
    eva = Bojovnik("Eva", 150, 40, 60, k)

    while adam.nazivu and eva.nazivu:
        adam.utok(eva)
        print(adam.getZprava())
        print(eva.getZprava())
        print(eva.graficky_zivot())
        
        if eva.nazivu:
            eva.utok(adam)
            print(eva.getZprava())
            print(adam.getZprava())
            print(adam.graficky_zivot())


