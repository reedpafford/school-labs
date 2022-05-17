def power(x,n):
    if n==0:
        return 1
    elif n<0:
        return (1/power(x,-n))
    elif n%2==0:
        return power(x,n/2)*power(x,n/2)
    elif n%2==1:
        return x*power(x,n//2)*power(x,n//2)

x = float(input('Enter a number: '))
n = float(input('Enter an integer between -100 and 100: '))
print('{} raised to the power of {} is {}'.format(x,n,power(x,n)))
