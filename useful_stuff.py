import pyodbc
import psycopg2


def connect_to_db_sql_server():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"  # Choose correct version of Driver. The same as your Server
        "SERVER=name_of_your_server;"
        "DATABASE=your_db_name;"
        "UID=your_user;"
        "PWD=your_password")
    yield conn.cursor()
    conn.close()


def connect_to_db_postgre():
    conn = psycopg2.connect(
        database="your_db_name",
        user='your_user',
        password='your_password',
        host='localhost',
        port='your_port'
    )
    yield conn.cursor()
    conn.close()
