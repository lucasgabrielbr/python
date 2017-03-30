'''#true or false - Boolean

var_verdade = True
var_falso = False

print(type(var_verdade), type(var_falso))

print(var_falso, type(var_falso))
'''
#Decision Making - Pt.1

'''var_verdade = True
var_falso = False

if var_verdade == True:
    print('Var_verdade is true!')
'''

#Decision Making - Pt.2

'''var_verdade = True
var_falso = False
'''
'''if 1 > 2 :
    print('1 is bigger than 2!')

if 2 > 1 :
    print('2 is bigger than 1!')

#Decision Making - Pt.3

a = 2
b = 1

if a > b :
    print(a,'is bigger than ',b,'!')

if b > a :
    print(b,'is bigger than',a,'!')

#Decision Making - Pt.4 - If / Else

a = 1
b = 2

if a > b :
    print(a,'is bigger than',b,'!')
else:
    print(a,'is not bigger than',b,'!')

#Decision Making - Pt.5 - If / Else com And/Or

#Example with 'and'
a = 3
b = 2

if a > b and 'python' == 'python':
    #It only runs if both conditions are true
    print('Both conditions were attended to!')
else:
    print('Some of the conditions were not met!')

#Example with 'or'
c = 3
d = 2

if c < d or 'hacker' != 'hacker':
    #Execute if any condition is true
    print('One or two conditions were met!')
else:
    print('Some or both conditions have not been met!')
'''

#Menus - Mode 1
'''print('Options: \n1 - Choose Lucas \n2 - Choose Gabriel \n3 - Choose Marcos \n')

option = input ('Choose one option:')

#Decision-making

if option == '1':
    print('Lucas')
if option == '2':
    print('Gabriel')
if option == '3':
    print('Marcos')

#this way(if,if,if), runs all if's
'''
#Menus - Mode 2

print('Options: \n1 - Choose Lucas \n2 - Choose Gabriel \n3 - Choose Marcos \n')

option = input ('Choose one option:')

#Decision-making

if option == '1':
    print('Lucas')
elif option == '2':
    print('Gabriel')
elif option == '3':
    print('Marcos')
else:
    print('Invalid Option')







