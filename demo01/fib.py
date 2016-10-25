# digui
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

number = int(input('Please enter the Fibs:'))
print fib(number)

#diedai
def fibs(a):
    n1 = 1
    n2 = 1
    n3 = 1

    if(a < 1):
        return -1

    while (a-2) > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        a -= 1

    return n3
result = fibs(20)

print result

