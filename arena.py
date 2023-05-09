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

    def zapas(self):
        print("Vitejte v Arene.")
        print(f"Dnes se utkaji {self.__bojovnik1} a {self.__bojovnik2}.")

        while self.__bojovnik1.nazivu and self.__bojovnik2.nazivu:
            self.__bojovnik1.utok(self.__bojovnik2)
            self.vypisZpravu(self.__bojovnik1.getZprava())
            self.vypisZpravu(self.__bojovnik2.getZprava())

            self.__bojovnik2.utok(self.__bojovnik1)
            self.vypisZpravu(self.__bojovnik2.getZprava())
            self.vypisZpravu(self.__bojovnik1.getZprava())

if __name__ == "__main__":
    k = kostka.Kostka(20)
    adam = bojovnik.Bojovnik("Adam", 100, 50, 40, k)
    martin = bojovnik.Bojovnik("Martin", 110, 60, 60, k)

    a = Arena(adam, martin, k)
    a.zapas()