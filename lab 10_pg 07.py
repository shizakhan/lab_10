print('shiza khan','18B-130-CS')
print('lab 10','program 07')
print('\n')
stu_info = {'name':'jibran','age':'12','class':'sixth','DOB':'16 april 2006',
            'school':'the seeds school','friend1':'mohib','friend2':'akbar',
            'friend3':'jaril'}

for x,y in stu_info.items():
    print(x,y)
stu_info.pop('friend1')
print(stu_info)
