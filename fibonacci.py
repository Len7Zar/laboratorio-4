
n=int(input("ingrese el numero de valores de la sucecion de fibonacci deseados"))
def fibonacci(val1,val2,n):
    if n>1:
        g=val1
        print (val1)
        val1=val1+val2
    
        fibonacci (val1,g,n-1)
    else:
        print (val1)
fibonacci (0,1,n)