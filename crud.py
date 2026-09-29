import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Connection
con = pymysql.connect(host="localhost", user="root", password="", cursorclass=pymysql.cursors.DictCursor)

# Cursor object
curobj = con.cursor()

# Code Functions
def cls():
    print("\n" * 4)

def intro():
    print('''+================================+
    SQL Data Management System (DMS)
+================================+''')

def menu():
    cls()
    intro()
    print(" Select a CRUD operation...")
    print(" 1. Create Database")
    print(" 2. Create table")
    print(" 3. Insert")
    print(" 4. Select All Records")
    print(" 5. Select columns Conditionally")
    print(" 6. Update")
    print(" 7. Delete table")
    print(" 8. Delete Database")
    print(" 9. Describe table")
    print(" S. Show Tables")
    print(" P. Plot a graph")
    print(" A. Alter")
    print(" E. Export")
    print(" Q. Quit")

def main():
    ch = input("Press 1 to 5 for CRUD or Q to Quit: ")
    if ch == '1':
        createdb()
    elif ch == 'S' or ch == 's':
        showtb()
    elif ch == '2':
        createtb()
    elif ch == '3':
        insert()
    elif ch == '4':
        selectall()
    elif ch == '5':
        selectcon()
    elif ch == '6':
        update()
    elif ch == '7':
        droptb()
    elif ch == '8':
        dropdb()
    elif ch == '9':
        desctb()
    elif ch == 'A' or ch == 'a':
        alter()
    elif ch == 'P' or ch == 'p':
        plot()
    elif ch == 'E' or ch == 'e':
        export()
    elif ch == 'Q' or ch == 'q':
        print("Thanks for using DMS!")
        curobj.close()
        con.close()
        return
    else:
        print("Invalid choice! Enter a valid option.")
        main()

def createdb():
    Q = input("Do you have a Database (y/n): ").lower()
    if Q == 'n':
        dname = input("Enter the database name: ")
        q1 = 'CREATE DATABASE {}'.format(dname)
        curobj.execute(q1)
    elif Q == 'y':
        dbn = input("Enter the Database name: ")
        q1 = 'USE {}'.format(dbn)
        curobj.execute(q1)

def createtb():
    db = input("Enter the database name: ")
    sql1 = 'USE {}'.format(db)
    curobj.execute(sql1)
    tb = input("Enter the table name: ")
    col = int(input("Enter the number of columns: "))
    sql = 'CREATE TABLE ' + tb + ' ('
    for i in range(col):
        colname = input("Enter the column name: ")
        print('''1. NUM
2. Alphabets
3. Date
4. Decimal''')
        datatype = input("Enter the datatype [num, alphabets, date, decimal]: ")
        if datatype == '1':
            datatype = 'int'
        elif datatype == '2':
            datatype = 'varchar'
        elif datatype == '3':
            datatype = 'date'
        elif datatype == '4':
            datatype = 'decimal'
        else:
            print('Invalid Choice!')
            continue
        constraint = input("Enter the constraint (leave blank for none): ")
        if datatype == 'decimal':
            x = int(input("Enter the characters before the decimal point: "))
            y = int(input("Enter the characters after the decimal point: "))
            size = str(x) + "," + str(y)
        else:
            size = input("Enter the length of the column: ")

        sql += colname + ' ' + datatype + '(' + size + ') ' + constraint + ','
    sql1 = sql[:-1]
    sql = sql1 + ')'
    print(sql)
    try:
        curobj.execute(sql)
        print('New table created')
    except con.Error as e:
        print("ERROR %d: %s" % (e.args[0], e.args[1]))

def showtb():
    db = input("Enter the database name: ")
    sql1 = 'USE {}'.format(db)
    curobj.execute(sql1)
    sql = "SHOW TABLES"
    curobj.execute(sql)
    tbn = curobj.fetchall()
    s1 = pd.DataFrame(tbn)
    print('''===================================
            Tables =''', list(s1['Tables_in_' + db]),
          '===================================')

def insert():
    db = input("Enter the database name: ")
    sql1 = 'USE {}'.format(db)
    curobj.execute(sql1)
    sql3 = 'SHOW TABLES'
    curobj.execute(sql3)
    result = curobj.fetchall()
    df = pd.DataFrame(result)
    colname = list(df['Tables_in_' + db])
    print('Tables =', colname)
    tbn = input("Enter the table name: ")
    sql2 = 'DESC {}'.format(tbn)
    curobj.execute(sql2)
    result = curobj.fetchall()
    df = pd.DataFrame(result)
    colname = list(df['Field'])
    sql = 'INSERT INTO ' + tbn + ' VALUES('
    for i in colname:
        x = input(i + ': ')
        sql += "'" + x + "',"
    sql = sql[:-1]
    sql += ')'
    print(sql)
    try:
        curobj.execute(sql)
    except con.Error as e:
        print("ERROR %d: %s" % (e.args[0], e.args[1]))

def selectall():
    db = input("Enter the database name: ")
    sql1 = 'USE {}'.format(db)
    curobj.execute(sql1)
    sql = "SHOW TABLES"
    curobj.execute(sql)
    tbnd = curobj.fetchall()
    s1 = pd.DataFrame(tbnd)
    print('Tables =', list(s1['Tables_in_' + db]))
    tbn = input("Enter the table name: ")

    sql = 'SELECT * FROM {}'.format(tbn)
    curobj.execute(sql)
    record = curobj.fetchall()
    result = pd.DataFrame(record)
    print(result)

def export():
    db = input("Enter the Database Name: ")
    sql = 'USE {}'.format(db)
    curobj.execute(sql)
    tbn = input("Enter the table name: ")
    sql = 'SELECT * FROM {}'.format(tbn)
    curobj.execute(sql)
    record = curobj.fetchall()
    result = pd.DataFrame(record)
    result.to_csv(f"{tbn}_data.csv", index=False)
    print(f"Data exported to {tbn}_data.csv")

def plot():
    db = input("Enter the database name: ")
    sql1 = 'USE {}'.format(db)
    curobj.execute(sql1)
    tbn = input("Enter the table name: ")
    sql = 'SELECT * FROM {}'.format(tbn)
    curobj.execute(sql)
    record = curobj.fetchall()
    result = pd.DataFrame(record)
    column = list(result.columns)
    print('Column Names:', column)
    bartype = input("Enter the bar Type[Bar, Line]: ").lower()
    title = input("Enter the title for the graph: ")
    x_axis = input("Enter the x-axis column name: ")
    y_axis = input("Enter the y-axis column name: ")
    colors = input("Enter the Bar colours: ")
    x = result[x_axis].tolist()
    y = result[y_axis].tolist()
    plt.title(title)
    if bartype == 'bar':
        outline = input('Enter the outline color: ')
        plt.bar(x, y, color=colors, width=0.5, edgecolor=outline)
    elif bartype == 'line':
        plt.plot(x, y, color=colors)
    else:
        print("Invalid Choice...")
        return
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.xticks(x)
    ymin = int(input("Enter the minimum y-axis value: "))
    ymax = int(input("Enter the maximum y-axis value: "))
    yinter = int(input("Enter the interval of y-axis: "))
    plt.yticks(np.arange(ymin, ymax, yinter))
    plt.show()

def dropdb():
    db = input("Enter the database name to delete: ")
    sql = 'DROP DATABASE {}'.format(db)
    curobj.execute(sql)
    print("Database successfully deleted...")

if __name__ == '__main__':
    main()
