#without fernet
def view():
    pass
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            l=line.rstrip()
            user,pwd=l.split('|')
            print('User:',user + ';'+ ' Password:',pwd)


def add():
#    pass
    name=input('enter your name:')
    pwd=input('enter your password:')
    with open('passwords.txt','a') as f:
        f.write(name+'|'+pwd+ '\n')
        

while True:
    choice=input("enter your choice to either view the password or add the password or quit (view/add/q):").lower()
    if choice=='q':
        print('thanks')
        break
    elif choice=='view':
        view()
    elif choice=='add':
        add()
    else:
        print('enter a valid input')
        continue