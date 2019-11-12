import subprocess as sp 
import pymysql
import pymysql.cursors



def createTeamMember():
    try:
        inputs = {}
        print("Enter team member's details: ")
        name = (input("Name (First Name, Last Name): ")).split(' ')
        inputs["first_name"] = name [0]
        inputs["last_name"] = name [1]
        inputs["roll_number"] = input("Roll Number: ")
        inputs["email"] = input("Email Address: ")
        inputs["contact_number"] = input("Contact Number: ")
        works = (input("Work ID: ")).split(' ')
        
        query1 = "INSERT INTO team_members(first_name, last_name, roll_number, email, contact_number) VALUES('%s', '%s', '%d', '%s', '%d')" %(inputs["first_name"], inputs["last_name"], inputs["roll_number"], inputs["email"], inputs["contact_number"])

        print(query1)
        cur.execute(query1)
        con.commit()

        for work in works:
            query2 = "INSERT INTO works(roll_number, job_id) VALUES('%d', '%s')" %(inputs["roll_number"], work)
            print(query2)
            cur.execute(query2)
            con.commit()
        print("Team Member Added To The Database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to insert into database')
        print('Error {!r}, Error Number {}'.format(e, e.args[0]))



def createFunders():
    try:
        inputs = {}
        print("Enter funder's details: ")
        name = (input("Name (First Name, Last Name): ")).split(' ')
        inputs["first_name"] = name [0]
        inputs["last_name"] = name [1]
        inputs["roll_number"] = input("Roll Number: ")
        inputs["email"] = input("Email Address: ")
        inputs["contact_number"] = input("Contact Number: ")
        
        query = "INSERT INTO funders(first_name, last_name, roll_number, email, contact_number) VALUES('%s', '%s', '%d', '%s', '%d')" %(inputs["first_name"], inputs["last_name"], inputs["roll_number"], inputs["email"], inputs["contact_number"])
        
        print(query)
        cur.execute(query)
        con.commit()

        print("Funder's Details Added To The Database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to insert into database')
        print('Error {!r}, Error Number {}'.format(e, e.args[0])) 



def addFundings():
    try:
        inputs = {}
        print("Enter funding details: ")
        inputs["roll_number"] = input("Roll Number: ")
        inputs["date"] = input("Date (YYYY-MM-DD): ")
        inputs["amount"] = input("Amount in INR: ")
        inputs["mode"] = input("Mode: ")
        inputs["transaction_id"] = input("Transaction ID: ")

        query = "INSERT INTO fundings(roll_number, date, amount, mode, transaction_id) VALUES('%d', '%s', '%d', '%s', '%s')" %(inputs["roll_number"], inputs["date"], inputs["amount"], inputs["mode"], inputs["transaction_id"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Funding added to the database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to insert into database')
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

        temp = input("Enter any key to continue> ")

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
                temp = input("Enter any key to contine> ")

    except:
        temp = sp.call('clear', shell=True)
        print("Connection Refused: Invalid credentials or Permission Denied")
        option = input("Enter exit to exit and anything else continue> ")
        if option == 'exit':
            break
