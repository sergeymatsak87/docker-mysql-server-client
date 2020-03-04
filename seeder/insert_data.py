import os
import time
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host=os.getenv('MYSQL_HOST'),
                                         database=os.getenv('MYSQL_DATABASE'),
                                         user=os.getenv('MYSQL_USER'),
                                         password=os.getenv('MYSQL_PASSWORD'))

    while True:
        now = datetime.now()
        formated_date = now.strftime('%Y-%m-%d %H:%M:%S')
        mysql_insert_query = """INSERT INTO ticks (created_at) VALUES ('%s')"""  % formated_date

        cursor = connection.cursor()
        cursor.execute(mysql_insert_query)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into ticks table", flush=False)
        cursor.close()
        time.sleep(1)

except mysql.connector.Error as error:
    print("Failed to insert record into ticks table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")