with open('learning_python.txt') as myfile:
    print(myfile.read())
    myfile.seek(0)
    for line in myfile:
        print(line)
    myfile.seek(0)
    listlines = myfile.readlines()

print(listlines)
   
