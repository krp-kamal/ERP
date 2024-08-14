'''
Author: Ms Rya
Version: 3.10
'''
display_size= {}
i=0
while(i<5):
    name = input('enter your name:')
    address = input('enter your IP adress:')
    display_size[name]= address
    i +=1
for var in display_size:
    print('{}\t{}'.format(var,display_size[var]))
print('size of dict:{}'.format(display_size))
