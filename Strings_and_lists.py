# Strings and lists

phrase = 'Hi, is it all right?'
print(phrase)

#Count the letters of the phrase
print(len(phrase))

#All lowercase letters. But it does not change the original phrase
print(phrase.lower())

#All upperercase letters. But it does not change the original phrase
print(phrase.upper())

#Prints a character, always starting from index "0"
print(phrase[12])

#Concatenate phrases
phrase2 = phrase + 'Yes, and you??'
print(phrase2)

#Prints the separate sentence at the point of interest
print(phrase.split('r'))

#Prints a range of characters [x: x]
print(phrase[4:10])

#Prints a range of characters with step [x: x: x]
print(phrase[0:10:2])

#Print the opposite sentence [x: x: x]
print(phrase[::-1])

#list

list_names = ['John','Mary','Lucas','Marcos']
print(list_names)
print(type(list_names))

#Print item 'x' from the list - index
#Can mix types in lists - Integer / Strings / Float / lists within lists
print(list_names[2])

#Print a range from the list - does not print the last item in the selected range
print(list_names[0:2])

#Print from last item - alternate order
print(list_names[-1])

#Print from last to first item
print(list_names[-1:-5:-1])

#Add name to list
list_names.append('Sebastian')
print(list_names)

list_names.append('Tiao')
print(list_names)

list_names.append('Johann')
print(list_names)

count_johann = list_names.count('Johann')
print(count_johann)

#Insert Method
list_names.insert(1, 'Gabriel')
print(list_names)

#Insert name in specific index
list_names[3] = 'Pythonino'
print(list_names)

#Remove name from list
list_names.remove('John')
print(list_names)

#POP Method - Displays the last term and removes it from the list
print(list_names.pop())
print(list_names)

#Count the items in the list
print(len(list_names))

#Delete entire list
list_names.clear()
print(list_names)

