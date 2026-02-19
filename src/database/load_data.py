import pandas as pd
from src.database.mysql_connection import get_connection


def load_transactions():

    conn = get_connection()

    query = "SELECT * FROM transactions"

    df = pd.read_sql(query, conn)

    # basic cleaning
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)


    conn.close()

    return df


if __name__ == "__main__":

    df = load_transactions()

    print(df.head())
