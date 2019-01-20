print('shiza khan','18B-130-CS(A)')
print('lab 10','Exercise Q#1')
print('\n')
#print a dictionary of your family then update it with your grandparents.
#also include uncles and aunts then print updated dictionary.
family = {'father':'Sohail Ahmed Khan','mother':'Shumaila','sister':'Waniya',
          'brother':'Shawaiz'}
print(family)
family['paternal_father'] = 'Aziz Ahmed Khan'
family['paternal_mother'] = 'Waliya Khatoon'
family['maternal_father'] = 'Abdul Waheed'
family['maternal_mother'] = 'Sumera'
family['paternal_aunt'] = 'Shahida'
family['paternal_uncle'] = 'Moin'
family['maternal_aunt'] = 'Humaira'
family['maternal_uncle'] = 'Haroon'
print('\n')
print('dictionary after updating: ',family)
