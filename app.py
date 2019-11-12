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


def createFunder():
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


def addFunding():
    try:
        inputs = {}
        print("Enter funding details: ")
        inputs["roll_number"] = input("Roll Number: ")
        inputs["date"] = input("Date and Time (YYYY-MM-DD HH:MM:SS) ")
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


def createProduct():
    try:
        inputs = {}
        print("Enter product details: ")
        inputs["product_id"] = input("Product ID: ")
        inputs["product_category"] = input("Product Category: ")
        inputs["product_name"] = input("Product Name: ")
        inputs["product_mrp"] = input("Product MRP: ")

        query = "INSERT INTO products(product_id, product_category, product_name, product_mrp) VALUES('%s', '%s', '%s', '%f')" %(inputs["product_id"], inputs["products_category"], input["product_name"], input["product_mrp"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Product added to the database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to insert into database')
        print('Error {!r}, Error Number {}'.format(e, e.args[0]))


def addProcurement():
    try:
        inputs = {}
        print("Enter procurement details: ")
        inputs["product_id"] = input("Product ID: ")
        inputs["date"] = input("Date (YYYY-MM-DD): ")
        inputs["vendor"] = input("Vendor Name: ")
        inputs["quantity"] = int(input("Quantity: "))
        inputs["total_cost"] = float(input("Total Cost: "))

        query = "INSERT INTO procurement(product_id, date, vendor, quantity, total_cost) VALUES('%s', '%s', '%s', '%d', '%f')" %(inputs["product_id"], inputs["date"], inputs["vendor"], inputs["quantity"], inputs["total_cost"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Procurement added to the database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to insert into database')
        print('Error {!r}, Error Number {}'.format(e, e.args[0]))


def addSales():
    try:
        inputs = {}
        print("Enter sales details: ")
        inputs["product_id"] = input("Product Id: ")
        inputs["date"] = input("Date (YYYY-MM-DD): ")
        inputs["quantity_before_sales"] = int(input("Quantity Before Sales: "))
        inputs["quantity_after_sales"] = inputs["quantity_after_sales"]

        query = "INSERT INTO sales(product_id, date, quantity_before_sales, quantity_after_sales) VALUES('%s', '%s', '%d', '%d')" %(inputs["product_id"], inputs["date"], inputs["quantity_before_sales"], inputs["quantity_after_sales"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Initial sales details added to the database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to insert into database')
        print('Error {!r}, Error Number {}'.format(e, e.args[0]))


def updateSales():
    try:
        input_date = input("Enter a date (YYYY-MM-DD): ")
        query = "SELECT * FROM sales WHERE date = '%s'" %(input_date)
        targets = cur.execute(query).fetchall()

        for target in targets:
            target = target.split(' ')
            print("Product ID: '%s' Quantity Before Sales: '%d' Quantity After Sales: '%d'" %(target[0], target[2], target[2]))
            choice = input("Want to change quantity before sales? [y/n] ")
            if choice == 'y':
                target[2] = int(input("Updated Quantity Before Sales: "))
            target[3] = int(input("Updated Quantity After Sales: "))
            query1 = "UPDATE sales SET quantity_before_sales = '%d', quantity_after_sales = '%d' WHERE date = '%s' AND product_id = '%s'" %(target[2], target[3], target[1], target[0])
            cur.execute(query1)
            con.commit()
        print("Sales details updated to the database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to update the database')
        print('Error {!r}, Error Number {}'.format(e, e.args[0]))


def addAccount():
    try:
        input_date = input("Enter a date (YYYY-MM-DD): ")
        query = "SELECT * FROM sales WHERE date = '%s'" %(input_date)
        targets = cur.execute(query).fetchall()
        total_expected_revenue = 0

        for target in targets:
            target = target.split(' ')
            query1 = "SELECT P.product_mrp * S.quantity_before_sales FROM product AS P, sales AS S WHERE P.product_id = '%s' AND S.product_id = '%s' AND S.date = '%s'" %(target[0], target[0], target[1])
            total_expected_revenue += cur.execute(query1).fetchone()
            con.commit()
            query2 ="UPDATE sales SET expected_revenue = '%f' WHERE date = '%s' AND product_id = '%s'" %(total_expected_revenue, target[1], target[0])
            cur.execute(query2)
            con.commit()
        print("Accounts are updated to the database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to update the database')
        print('Error {!r}, Error Number {}'.format(e, e.args[0]))
            
def finalAccount():
    try:
        input_date = input("Enter a date (YYYY-MM-DD): ")
        query = "SELECT * FROM sales WHERE date = '%s'" %(input_date)
        targets = cur.execute(query).fetchall()
        total_expected_revenue = 0

        for target in targets:
            target = target.split(' ')
            query1 = "SELECT P.product_mrp * (S.quantity_before_sales - S.quantity_after_sales) FROM product AS P, sales AS S WHERE P.product_id = '%s' AND S.product_id = '%s' AND S.date = '%s'" %(target[0], target[0], target[1])
            total_expected_revenue += float(cur.execute(query1).fetchone())
            con.commit()
            query2 ="UPDATE sales SET expected_revenue = '%f' WHERE date = '%s' AND product_id = '%s'" %(total_expected_revenue, target[1], target[0])
            cur.execute(query2)
            con.commit()
        print("Accounts are updated to the database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to update the database')
        print('Error {!r}, Error Number {}'.format(e, e.args[0]))

def updateAccount():
    try:
        input_date = input("Enter a date (YYYY-MM-DD): ")
        actual_revenue = float(input("Actual Revenue in INR: "))

        query = "UPDATE accounts SET actual_revenue = '%f' WHERE date = '%s'" %(actual_revenue, input_date)
        cur.execute(query)
        con.commit()
        print("Actual revenue updated in the database")
    except pymysql.Error as e:
        con.rollback()
        print('Failed to update the database')
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
