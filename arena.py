#!/usr/bin/env python3

import bojovnik
import kostka

class Arena():

    def __init__(self, bojovnik1, bojovnik2, kostka):
        self.__bojovnik1 = bojovnik1
        self.__bojovnik2 = bojovnik2
        self.__kostka = kostka

    def zapas(self):
        pass

if __name__ == "__main__":
    k = kostka.Koskta(20)
    adam = bojovnik.Bojovnik("Adam", 100, 50, 40, k)
    martin = bojovnik.Bojovnik("Martin", 110, 60, 60, k)

    a = Arena(adam, martin, k)
    a.zapas()