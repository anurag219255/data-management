# def __init__.py
#here we are integrating the read part and the write part

#modifying file in the app

import os
import sys

from read import get_json_reader
from write import load_db_table  #press control space to list the functions in the programs


def process_table(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])


def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    table_names = sys.argv[1].split(',')#it will access first argument pass to the program so we are passing 1
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'

    for table_name in table_names:
        process_table(BASE_DIR, conn, table_name)


if __name__=='__main__':
    main()





