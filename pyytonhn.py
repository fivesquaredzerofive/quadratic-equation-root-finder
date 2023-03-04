import math
equation = str(input("Enter the quadratic equation (ax^2+bx+c): "))
eq2 = equation
loc = equation.find("x")
al = eq2[:loc]
eq2 = equation[loc+3:]
loc = eq2.find("x")
bl = eq2[:loc]
eq2 = eq2[loc+1:]
cl = eq2
if al == "":
    al = 1
if bl == "":
    bl = 1
if cl == "":
    cl = 1
al = float(al)
bl = float(bl)
cl = float(cl)
discr = (bl**2)-(4*al*cl)
if discr < 0:
    print("No real root exists.")
else :
    fr = ((-1*bl)+math.sqrt(discr))/(2*al)
    sr = ((-1*bl)-math.sqrt(discr))/(2*al)

    print("Root one is : %.5f \nRoot two is : %.5f"%(fr,sr))