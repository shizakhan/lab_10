print('shiza khan','18B-130-CS')
print('lab 10','program 09')
print('\n')
#removing items from the dictionary using pop()
stu_info = {'name':'jibran','age':'12','class':'sixth','DOB':'16 april 2006',
            'school':'the seeds school','friend1':'mohib','friend2':'akbar',
            'friend3':'jaril'}

for x,y in stu_info.items():
    print(x,y)
stu_info.popitem()
print("after poping from the dictionary the remaining elements are: ",stu_info) 
