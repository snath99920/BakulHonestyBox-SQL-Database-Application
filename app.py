import subprocess as sp 
import pymysql
import pymysql.cursors

def createTeamMember():
    try:
        input = {}
        print("Enter team member's details: ")
        name = (input("Name (First Name, Last Name): ")).split(' ')
        input["first_name"] = name [0]
        input["last_name"] = name [1]
        input["roll_number"] = input("Roll Number: ")
        input["email"] = input("Email Address: ")
        input["contact_number"] = input("Contact Number: ")
        works = (input("Work ID: ")).split(' ')
        
        query1 = "INSERT INTO team_members(first_name, last_name, roll_number, email, contact_number) VALUES('%s', '%s', '%d', '%s', '%d')" %(input["first_name"], input["last_name"], input["roll_number"], input["email"], input["contact_number"])

        print(query1)
        cur.execute(query1)
        con.commit()

        for work in works:
            query2 = "INSERT INTO works(roll_number, job_id) VALUES('%d', '%s')" %(input["roll_number"], work)
            print(query2)
            cur.execute(query2)
            con.commit()
        print("Team Member Added To The Database")
    except pymysql.Error as e:
        print('Error {!r}, Error Number {}'.format(e, e.args[0]))

while(True):
    temp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        temp = sp.call('clear', shell=True)
        con = pymysql.connect(
            host = 'localhost',
            user = username,
            password = password,
            db = 'BHB',
            cursorclass = pymysql.cursors.DictCursor
        )
        temp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to Connect")

        temp = input("Enter any key to continue")

        with con:
            cur = con.cursor()
            while(1):
                temp = sp.call('clear', shell=True)

                choice = int(input("Enter an option: "))
                temp = sp.call('clear', shell=True)

                if choice == 5:
                    break
                else:
                    dispatch(choice)
                temp = input("Enter any key to contine")

    except:
        temp = sp.call('clear', shell=True)
        print("Connection Refused: Invalid credentials or Permission Denied")
        option = input("Enter exit to exit, else continue ")
        if option == 'exit':
            break




