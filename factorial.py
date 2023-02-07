n=int (input('Enter any number:'))

def factorial(n):
    fctrl=1
    if n==0 or n==1:
        return 1
    for i in range(1,n+1):
        fctrl=fctrl*i
    return fctrl

rslt=factorial(n)
print('Factorial of number ' , n,' is : ',rslt)