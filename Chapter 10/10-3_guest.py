nameofuser = input('Hi what is your name')
with open('guest.txt', 'w') as guestfile:
    guestfile.write(nameofuser)
