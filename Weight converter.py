weight = int(input('weight: '))
unit = input('(L)bs  or (k)gs : ')
if unit.upper() == 'L':
    convert=weight*0.45
    print('your weight is'+ str(convert) + 'in kgs')
elif unit.upper()=='K' :
    
    convert=weight/0.45
    print("your weight is  " +  str(convert)  + ' in pounds')
else:
    print('Please enter correct unit')
