#!/usr/bin/env python3

morse = {
    "a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....",
    "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.",
    "q":"--.-", "r":".-.", "s":"...", "t":"-", "v":"...-", "w":".--", "x":"-..-",
    "y":"-.--", "z":"--..", " ":""
}

vstup = input("Zadej text: ")

for pismeno in vstup:
    try:
        print(morse[pismeno.lower()] + "/", end="")
    except:
        print("?/", end="")
print("//")


