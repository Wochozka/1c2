#!/usr/bin/env python3

import random

class Kostka:
    """
    Trida reprezentujici hraci kostku.
    """

    def __init__(self, pocetSten=6):
        try:
            if (pocetSten > 1):
                self.pocetSten = pocetSten
            else:
                print("Kostka musi mit vice nez 1 stenu.")
                exit(2)
        except:
            print("Kostku nelze vytvorit.")
            exit(2)
    
    def hod(self):
        try:
            return random.randint(1,self.pocetSten)
        except:
            return "Kostkou nelze hodit."

    def __str__(self):
        return f"Kostka s {self.pocetSten} stenami."

if __name__ == "__main__":
    k = Kostka()
    print(k.hod())
    print(k)