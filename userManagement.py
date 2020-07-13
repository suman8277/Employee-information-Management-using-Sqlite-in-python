import  sqliteDemo

mydb =sqliteDemo.MyDatabase('EmployeeInfo.db')
mydb.create_table()
#mydb.insert_data()

while True:
    print('1)Insert Data')
    print('2)Delete Data')
    print('3)Update Data')
    print('4)select Data')
    print('5)exit')
    x= int(input('select your choice: '))
    if x==1:
        name = input('enter Employee name:')
        number = input('enter Employee number:')
        mydb.insert_data(name,number)

    elif x==2:
        id = input('enter id: ')
        mydb.delete_data(id)
        print("successfully deleted")

    elif x==3:
        while True:
            print('1)Update Name: ')
            print('2)Update Number: ')
            print('0)exit')
            y=int(input('Enter your choice: '))
            if y==1:
                id = input('enter id: ')
                name = input('enter name:')
                mydb.update_name(name , id)
            elif y==2:
                id = input('enter id: ')
                number = input('enter the Number: ')
                mydb.update_number(number,id)
            elif y==0:
                break

            else:
                print("invalid input")




    elif x==4:
        mydb.select_data()

    elif x==5:
        break

    else:
        print('invalid input')

