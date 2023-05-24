from sympy import *


x = symbols("x")
input_function = input("Enter your function:\n")
function = eval(input_function)

input_start = input("Enter starting point. Can not be zero!\n")
start = float(input_start)


ableitung = diff(function)
print(ableitung)


def newton_methode(funktion, ableitung, vorherigerwert):
    newton_funkt = x-(funktion/ableitung)
    ergebnis = newton_funkt.evalf(subs={x: vorherigerwert})
    return ergebnis


wert_alt = start
while true:
    wert_neu = newton_methode(function, ableitung, wert_alt)
    if wert_alt-wert_neu < 0.000001:
        wert_alt = wert_neu
        break
    wert_alt = wert_neu

print(wert_alt)
