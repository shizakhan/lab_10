print('shiza khan','18B-130-CS(A)')
print('lab 10','Exercise Q#2')
print('\n')
#design a phone directory of your parents and friends
#then make a function to delete a member from phone directory
#print total number of members in your personal phone directory
ph_direct = {'father':'03333010639','mother':'03331360684','friend1':'03363077057',
             'friend2':'03122765190','friend3':'03032989289','friend4':'0300066927',
             'friend5':'03063616349','friend6':'03132409687','friend7':'04238900927',
             'friend8':'03012960053','friend9':'03331360685','friend10':'03363077056'}
print(ph_direct)
def del_dict(ph_direct):
    choose = input('what phone number you want to delete ?')
    ph_direct.pop(choose)
    print('my personal phone directory is: ',ph_direct)

    
