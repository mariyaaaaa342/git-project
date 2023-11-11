from math import *
c = int(input("c = "))
x = float(input("x = "))
match c:
    case 1:
        a = -1.2
        b = 0.75
        z = log(abs(tan(b * x)))
        if x <= a:
            y = a+sin(b*x)+cos(x**2)
        elif a < x < log(b):
            y = sqrt(a+b*x)+sin(x*z)
        else: y = log(a + b * x + z)
        print("y=",round(y,3))
    case 2:
        a = 0.4
        b = 2.4
        z = log(abs(tan(b * x)))
        if a < x <log(b):
            y = a+sin(b*x)+cos(x**2)
        elif a < x < log(b):
            y = sqrt(a + b * x) + sin(x * z)
        else: y = log(a + b * x + z)
        print(round(y, 3))
    case 3:
        a = 1.1
        b = 6.1
        z = log10(abs(tan(b * x)))
        if x >= log(b):
            y = a+sin(b*x)+cos(x**2)
        elif a < x < log(b):
            y = sqrt(a + b * x) + sin(x * z)
        else: y = log(a + b * x + z)
        print(round(y, 3))
    case _: print("error")