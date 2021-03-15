userNameList = ['ambik', 'akkuu', 'pikul', 'jochi', 'froti'] # existing users
id=0
while(True):
    userChoice = input('New user ? (Yes / No): ')
    if userChoice in ('Yes', 'yes'): # checking whether new user or not
        firstName = input('Enter your first name: ')
        lastName = input('Enter your last name: ')
        newUserName = firstName[0:3] + lastName[0:2] # getting the first 3 letters from first name and last 2 letters from last name
        print(userNameList)
        if newUserName in userNameList:
            id+=1
            I=userNameList.index(newUserName)
            print('Your user name is: ', newUserName+userNameList[I]+str(id))
            userNameList.append(newUserName+userNameList[I]+str(id))
            print('User added!\n')
        else:
            print('Your user name is: ', newUserName)
            userNameList.append(newUserName)
            print('User added!\n')

    elif userChoice in ('No', 'no'): # if existing user then execute this block
        c=0
        while (c<3): 
            
            c+=1   
            username = input('Enter your username: ')
            if username in userNameList:
                print('Access Granted\n')
                break 

            elif(c==3):
                print('Access denied')    