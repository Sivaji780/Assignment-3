def u_l(string):
    output = {'upper':0, 'lower':0}
    for letter in string:
        if letter.isupper():
            output['upper']=output['upper']+1
        if letter.islower():
            output['lower']=output['lower']+1
    print('upper:',output['upper'])
    print('lower:',output['lower'])
    
string = input()
u_l(string)