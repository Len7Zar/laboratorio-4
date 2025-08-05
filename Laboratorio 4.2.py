divisor=int(input("ingrese un numero para hacer de divisor"))
n=int(input("ingrese un numero para averiguar si es primo o no"))
def is_prime(n, divisor):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

print(is_prime(n,divisor)) 
