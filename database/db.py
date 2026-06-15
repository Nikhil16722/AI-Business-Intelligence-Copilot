import sqlite3

def save_to_db(df):

    conn = sqlite3.connect(
        "business.db"
    )

    df.to_sql(
        "sales",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()