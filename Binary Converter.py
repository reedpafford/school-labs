def ToBinary(x):
    x=int(x)
    binary=''
    while x>0:
        binary=binary+str(x%2)
        x=x//2
    return binary[::-1]

def binaryAdd(a,b):
    max_len=max(len(a),len(b))
    a=a.zfill(max_len)
    b=b.zfill(max_len)
    result=''
    carry=0
    for i in range(max_len - 1,-1,-1):
        remainder=carry
        remainder+=1 if a[i]=='1' else 0
        remainder+=1 if b[i]=='1' else 0
        result=('1' if remainder%2==1 else '0') + result
        carry = 0 if remainder < 2 else 1
    if carry !=0:
        result='1' + result
    return result.zfill(max_len)
    

nums=[int(i) for i in input('Enter integers to be added: ').split(' ')]
t='0'
for i in range(len(nums)):
    t=binaryAdd(t,ToBinary(nums[i]))
print(t)
