import os
import time
from datetime import datetime


host=os.getenv('MYSQL_HOST')
database=os.getenv('MYSQL_DATABASE')
user=os.getenv('MYSQL_USER')
password=os.getenv('MYSQL_PASSWORD')

counter = 0

while True:
    if (counter == 5):
        now = datetime.now()
        formated_date = now.strftime('%Y-%m-%d_%H-%M-%S')
        print("Starting MySQL Backup " + formated_date, flush=True)
        print("MySQL Backup failed", flush=True)
        print()
        time.sleep(5)
        counter = 0
    else:
        now = datetime.now()
        formated_date = now.strftime('%Y-%m-%d_%H-%M-%S')
        print("Starting MySQL Backup " + formated_date, flush=True)
        os.system("mysqldump -h " + host + " -u" + user + " -p" + password + " " + database + " ticks | gzip > /backup/db_" + formated_date + ".sql.gz")
        print("MySQL Backup finished successfully", flush=True)
        print()
        time.sleep(5)
    counter += 1

