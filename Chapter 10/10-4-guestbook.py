while True:
    guest_name = input('Please enter your name: ')
    if guest_name == 'quit':
        break
    with open('guest_book.txt', 'a') as guestbook:
        guestbook.write(guest_name+'\n')
