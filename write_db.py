import psycopg2
from sml_parser import parse
import pandas as pd

database = "iotdb"
user = 'pi',
password = 'pw_raspberry'
host = '127.0.0.1'
port = '5432'

table_name = "ENERGYMGMT"

# Connect to an existing database
connection = psycopg2.connect(user="pi",
                              password="pw_raspberry",
                              host="127.0.0.1",
                              port="5432",
                              database="iotdb")

def write_to_db(data):
    parsed = data
    date = pd.to_datetime(parsed[0]['date'])
    power = float(parsed[3]['CR_P'])
    insert_query = """ INSERT INTO ENERGYMGMT (DATE, POWER) VALUES (%s, %s)"""
    item_tuple = (date, power)
    cursor = connection.cursor()
    cursor.execute(insert_query, item_tuple)
    connection.commit()
