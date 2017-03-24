#Data in/out
#Output files

#print- Print on the screen
print('Hello World!')
print("Hello Mr. Sebastian")
print("---------------------------------------------------------------")

#Multiple lines in a single printt
print('Hello World! \n Second Print')

#Tab in a single print
print('Hello World! \t Second Print')
print("---------------------------------------------------------------")
#Variables - dynamic typing - You do not need to declare the variable type

#String - text
name = 'Lucas'
print(name)
print("---------------------------------------------------------------")

#String with type
name = 'Lucas'
print(type(name))
print("---------------------------------------------------------------")

#Variable Integer with type
age = 32
print(age)
print(type(age))
print("---------------------------------------------------------------")

#Variable Float with type
value = 10.2
print(value)
print(type(value))
print("---------------------------------------------------------------")

#Composite print - Concatenate

print(name, 'as\n', age, 'years old!')
print("---------------------------------------------------------------")
#Composite print

#print(name, 'as\n', age, 'years old!')
# there will be a problem with age(int) with name(str)

#correction - Convert age to string
print(name + ' is ' + str(age) + ' years old!')
print("---------------------------------------------------------------")

#Data input

name2 = input('Type your name: ')
age2 = input('Type your age: ')
print('Hello ',name2,'.','You are: ',age2, 'years old!')
print("---------------------------------------------------------------")

#Basic Calculations

n1 = 27
n2 = 53

print(n1 + n2)
print("---------------------------------------------------------------")

#test with data entry

n1 = input('Enter the first number of the sum: ')
n2 = input('Enter the second number of the sum: ')
sum = int(n1) + int(n2)
print(type(sum))
print('The sum is: ',sum)
print(type(sum),type(n1),type(n2))
print("---------------------------------------------------------------")


