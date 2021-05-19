"""
18. Write a program to generate SQLException
"""

try:
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",
    database='student')
    mycursor = mydb.cursor()
    sql = "UPDATE students SET address = 'Canyon 123' WHERE address = 'Valley 345'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
except mysql.connector.errors.ProgrammingError as msl:
    print(msl)
