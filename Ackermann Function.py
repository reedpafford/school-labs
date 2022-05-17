def ackermann(m,n):
    if m==0:
        return n+1
    if n==0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m,n-1))
    
p=int(input('Enter value for m: '))
q=int(input('Enter a value for n: '))
print('Ackermann({},{}) = {}'.format(p,q,ackermann(p,q)))
