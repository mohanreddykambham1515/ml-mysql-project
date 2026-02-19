import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="7981529509",
        database="fraud_db"
    )

    return conn
