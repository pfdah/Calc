import re

print('Welcome Hooman\nThis is a calculator')
print('Type \'quit\' to exit')

run = True
previous  = 0


def calc():
    global run
    global previous
    if previous == 0:
        eqn = input('Enter the required equation : \n').strip().lower()
    else:
        eqn = input(str(previous))
    if eqn == 'quit':
        print('Bye bye Hooman')
        run = False
    else:
        eqn = re.sub('[a-zA-Z;,:"\']','',eqn)
       
        if previous == 0:
            previous = eval(eqn)
        else:
            previous = eval(str(previous)+eqn)
        
while run:
    calc()
