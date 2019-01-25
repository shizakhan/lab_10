print('shiza khan','18B-130-CS')
print('lab 10','programming exercise 5')
print('\n')
parents_guests = {'Mr.khalil':5 ,'Mr.Ashfaq':6,'Mr.Ahmed':4,'Mr.Haroon':3,
                  'Mr.moin':2}

my_guests = {'Sara':5,'Eman':4,'Mr.khalil':5,'Mr.Ahmed':4,'Urooj':3}

for x,y in parents_guests.items():
    for a,b in my_guests.items():
        if (x,y)==(a,b):
            print("common guests are: ",x,y)
print('\n')            
 
total = 0

for x in parents_guests.values():
    total = total + x

for y in my_guests.values():
    total = total + y
print("The total number of guest are " +str(total))

