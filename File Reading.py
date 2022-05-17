
user_file=input('Please enter the name of the file: ')
try:
    f=open(user_file,'r')
    lines=f.readlines()
    upper_count=0
    lower_count=0
    digit_count=0
    spaces_count=0
    for i in lines:
        for j in i:
            if j.isupper():
                upper_count+=1
            if j.islower():
                lower_count+=1
            if j.isdigit():
                digit_count+=1
            if j.isspace():
                spaces_count+=1
            else:
                continue
    print('Uppercase letters: ',upper_count)
    print('Lowercase letters: ',lower_count)
    print('Digits: ',digit_count)
    print('Spaces: ',spaces_count)
except FileNotFoundError:
    print('File not found')
