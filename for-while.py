'''

This is a program that reads the amount of guests who will be invited to a party.
After this, the program will ask the names of the guests and print the names of the guests

'''

# Program

num_guests = input('How many guests ?')
gests_list = []

i = 1

while i <= int(num_guests):
    guest_name = input('Guest number '+ str(i)+':')
    gests_list.append(guest_name)
    i += 1

print('There will be', num_guests,'guests!')

print('\nGuests List')

i1 = 1
for guest in gests_list:
    print('Guest ',i1,':',guest)
    i1 += 1
