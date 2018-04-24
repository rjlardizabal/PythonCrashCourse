while True:
    reason = input('Why do you like programming?: ')
    if reason == 'q':
        break
    with open('responses.txt', mode='a') as responseobj:
        responseobj.write(reason + '\n')
