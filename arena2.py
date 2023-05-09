#!/usr/bin/env python3

import bojovnik
import kostka

class Arena():

    def __init__(self, bojovnik1, bojovnik2, kostka):
        self.__bojovnik1 = bojovnik1
        self.__bojovnik2 = bojovnik2
        self.__kostka = kostka

    def vypisZpravu(self, zprava):
        import time as _time
        print(zprava)
        _time.sleep(1)
    
    def vykresli(self):
        self.vymazObrazovku()
        print("--------------- Arena ---------------\n")
        self.vykresliBojovnika(self.__bojovnik1)
        self.vykresliBojovnika(self.__bojovnik2)
    
    def vymazObrazovku(self):
        import subprocess
        subprocess.call("clear")
    
    def vykresliBojovnika(self, bojovnik):
        print(bojovnik)
        print(f"Zivot: {bojovnik.graficky_zivot()}")

    def zapas(self):
        print("Vitejte v Arene.")
        print(f"Dnes se utkaji {self.__bojovnik1} a {self.__bojovnik2}.")

        import random
        if (random.randint(0,1)):
            (self.__bojovnik1, self.__bojovnik2) = (self.__bojovnik2, self.__bojovnik1)

        while self.__bojovnik1.nazivu and self.__bojovnik2.nazivu:

            self.__bojovnik1.utok(self.__bojovnik2)
            self.vykresli()
            self.vypisZpravu(self.__bojovnik1.getZprava())
            self.vypisZpravu(self.__bojovnik2.getZprava())

            if self.__bojovnik2.nazivu:
                self.__bojovnik2.utok(self.__bojovnik1)
                self.vykresli()
                self.vypisZpravu(self.__bojovnik2.getZprava())
                self.vypisZpravu(self.__bojovnik1.getZprava())

if __name__ == "__main__":
    k = kostka.Kostka(20)
    
    print("Zdej udaje prvniho bojovnika:\n")
    jmeno1 = input("Jmeno:")
    zivot1 = int(input("zivot:"))
    utok1 = int(input("utok:"))
    obrana1 = int(input("obrana:"))
    adam = bojovnik.Bojovnik(jmeno1, zivot1, utok1, obrana1, k)

    print("Zdej udaje druheho bojovnika:\n")
    jmeno2 = input("Jmeno:")
    zivot2 = int(input("zivot:"))
    utok2 = int(input("utok:"))
    obrana2 = int(input("obrana:"))

    martin = bojovnik.Bojovnik(jmeno2, zivot2, utok2, obrana2, k)

    a = Arena(adam, martin, k)
    a.zapas()