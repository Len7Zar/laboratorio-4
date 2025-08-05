
x=int(input("ingrese la cantidad para ver la sumatoria desde 1 hasta el numero ingresado (n)"))
def sumatoria (x):
    if x==1:
        return 1
    else:
        return x+sumatoria(x-1)
print ("el resultado de su sumatoria es: ", sumatoria (x))