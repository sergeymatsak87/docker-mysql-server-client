import os
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host=os.getenv('MYSQL_HOST'),
                                         database=os.getenv('MYSQL_DATABASE'),
                                         user=os.getenv('MYSQL_USER'),
                                         password=os.getenv('MYSQL_PASSWORD'))

    mysql_create_table_query = """CREATE TABLE IF NOT EXISTS ticks (id int(10) NOT NULL AUTO_INCREMENT,
                                                                    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                                                    PRIMARY KEY (id)) """
    cursor = connection.cursor()
    result = cursor.execute(mysql_create_table_query)
    print("ticks table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")