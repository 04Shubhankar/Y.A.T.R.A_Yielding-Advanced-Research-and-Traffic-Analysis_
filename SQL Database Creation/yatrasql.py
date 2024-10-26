

import mysql.connector
from mysql.connector import errorcode

# Establish the connection
try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", #Password for SQL Workbench
        database="yatra"  #Name of Created data base
    )
    cursor = db_connection.cursor()

    # Check if the connection was successful
    if db_connection.is_connected():
        print("Successfully connected to the database")

    # Create a database using SQL query
    cursor.execute("CREATE DATABASE IF NOT EXISTS Yatra")
    cursor.execute("USE Yatra")

    # Create the Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            Pancard_no VARCHAR(10) PRIMARY KEY,
            Name VARCHAR(50) NOT NULL,
            Password VARCHAR(15) NOT NULL
        )
    """)

    # Define the SQL query for Users
    add_user = ("INSERT INTO Users (Pancard_no, Name, Password) VALUES (%s, %s, %s)")

    # Data to be inserted into Users
    data_users = [
        ('ABCDE1234F', 'Vicky Raina', 'password123'),
        ('FGHIJ5678K', 'Harshal Gupta', 'securePass!'),
        ('KLMNO9012P', 'Ali Johnson', 'alija@2024'),
        ('QRSTU3456V', 'Bobby Deol', 'bobSecure#1'),
        ('WXYZA7890B', 'Charlie Davis', 'charliePwd$'),
        ('BCDEF2345G', 'David Evans', 'david1234'),
        ('CDEFG3456H', 'Eva Green', 'evaPass!'),
        ('DEFGH4567I', 'Frank Harris', 'frank@2024'),
        ('EFGHI5678J', 'Grace Lad', 'graceSecure#1'),
        ('FGHIJ6789K', 'Hanklin Mehta', 'hankPwd$'),
        ('GHIJK7890L', 'Ivy Nelson', 'ivy1234'),
        ('HIJKL8901M', 'Jack Owens', 'jackPass!'),
        ('IJKLM9012N', 'Kara Peterson', 'kara@2024'),
        ('JKLMN0123O', 'Leo Quinn', 'leoSecure#1'),
        ('KLMNO1234P', 'Mia Roberts', 'miaPwd$'),
        ('LMNOP2345Q', 'Nina Scott', 'nina1234'),
        ('MNOPQ3456R', 'Oscar Turner', 'oscarPass!'),
        ('NOPQR4567S', 'Paul Underwood', 'paul@2024'),
        ('OPQRS5678T', 'Quinn Vance', 'quinnSecure#1'),
        ('PQRST6789U', 'Rita White', 'ritaPwd$'),
        ('QRSTU7890V', 'Sameer Taude', 'sam1234'),
        ('RSTUV8901W', 'Tina Singh', 'tinaPass!'),
        ('STUVW9012X', 'Allen Joseph', 'allen@2024'),
        ('TUVWX0123Y', 'Uzma Khan', 'uzmaSecure#1'),
        ('UVWXY1234Z', 'Wendy Dev', 'wendyPwd$'),
        ('VWXYZ2345A', 'Aishwarya Deshmukh', 'aish1234'),
        ('WXYZA3456B', 'Munira Badshah', 'yarraPass!'),
        ('XYZAB4567C', 'Aisiki Bain', 'zane@2024'),
        ('YZABC5678D', 'Nikita Jude', 'Nikky#1'),
        ('ZABCD6789E', 'Brian Harris', 'brianPwd$')
    ]

    # Execute the query for each data entry in Users
    for data_user in data_users:
        cursor.execute(add_user, data_user)

    # Create the Ownerinfo table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ownerinfo (
            Number_plate VARCHAR(20) PRIMARY KEY,
            Ownername VARCHAR(50) NOT NULL,
            Contact_no VARCHAR(15) NOT NULL
        )
    """)

    # Define the SQL query for Ownerinfo
    add_owner = ("INSERT INTO Ownerinfo (Number_plate, Ownername, Contact_no) VALUES (%s, %s, %s)")

    # Data to be inserted into Ownerinfo
    data_owners = [
        ('MH12AB1234', 'Vicky Raina', '9876543210'),
        ('MH14CD5678', 'Harshal Gupta', '8765432109'),
        ('MH15EF9012', 'Ali Johnson', '7654321098'),
        ('MH16GH3456', 'Bobby Deol', '8543210987'),
        ('MH17IJ7890', 'Charlie Davis', '8432109876'),
        ('MH18KL1234', 'David Evans', '8321098765'),
        ('MH19MN5678', 'Eva Green', '9210987654'),
        ('MH20OP9012', 'Frank Harris', '8109876543'),
        ('MH21QR3456', 'Grace Lad', '7098765432'),
        ('MH22ST7890', 'Hank Mehta', '9987654321'),
        ('MH23UV1234', 'Ivy Nelson', '9876543211'),
        ('MH24WX5678', 'Jack Owens', '8765432108'),
        ('MH25YZ9012', 'Kara Peterson', '7654321097'),
        ('MH26AB3456', 'Leo Quinn', '9543210986'),
        ('MH27CD7890', 'Mia Roberts', '9432109875'),
        ('MH28EF1234', 'Nina Scott', '9321098764'),
        ('MH29GH5678', 'Oscar Turner', '9210987653'),
        ('MH30IJ9012', 'Paul Underwood', '8109876542'),
        ('MH31KL3456', 'Quinn Vance', '7098765431'),
        ('MH32MN7890', 'Rita White', '8987654320'),
        ('MH33OP1234', 'Sameer Taude', '9876543212'),
        ('MH34QR5678', 'Tina Singh', '8765432107'),
        ('MH35ST9012', 'Allen Joseph', '7654321096'),
        ('MH36UV3456', 'Uzma Khan', '8543210985'),
        ('MH37WX7890', 'Wendy Dev', '8432109874'),
        ('MH38YZ1234', 'Aishwarya Deshmukh', '9321098763'),
        ('MH39AB5678', 'Munira Badshah', '9210987652'),
        ('MH40CD9012', 'Aishiki Bain', '7109876541'),
        ('MH41EF3456', 'Nikita Jude', '8098765430'),
        ('MH42GH7890', 'Brian Harris', '9487654329')
    ]

    # Execute the query for each data entry in Ownerinfo
    for data_owner in data_owners:
        cursor.execute(add_owner, data_owner)

    # Commit the transaction
    db_connection.commit()

    print("Values inserted into both tables")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    # Close the cursor and connection
    if db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("MySQL connection is closed")
