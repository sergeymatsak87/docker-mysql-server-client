import os
import time
import sys
from datetime import datetime

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout

    def write(self, message):
        with open ("/backup/logs/dbbackup.log", "a", encoding = 'utf-8') as self.log:
            self.log.write(message)
        self.terminal.write(message)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass
sys.stdout = Logger() 


host=os.getenv('MYSQL_HOST')
database=os.getenv('MYSQL_DATABASE')
user=os.getenv('MYSQL_USER')
password=os.getenv('MYSQL_PASSWORD')


counter = 0

while True:
    if (counter == 5):
        now = datetime.now()
        formated_date = now.strftime('%Y-%m-%d_%H-%M-%S')
        print("Starting MySQL Backup " + formated_date)
        print("MySQL Backup failed")
        print()
        time.sleep(5)
        counter = 0
    else:
        now = datetime.now()
        formated_date = now.strftime('%Y-%m-%d_%H-%M-%S')
        print("Starting MySQL Backup " + formated_date)
        os.system("mysqldump -h " + host + " -u" + user + " -p" + password + " " + database + " ticks | gzip > /backup/db_" + formated_date + ".sql.gz")
        print("MySQL Backup finished successfully")
        print()
        time.sleep(5)
    counter += 1


