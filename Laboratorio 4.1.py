print ("bienvenidos al laboratorio 4")
n=int(input("ingrese el numero para obtener su factorial"))
def factorial(n):
    print("me estoy llamando a mi mismo, el valor de n ahora es:", n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(n))