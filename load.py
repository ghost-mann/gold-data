import sqlite3

def load_data(df, db_name='xauusd_data.db'):
    conn = sqlite3.connect(db_name)
    df.to_sql('xauusd_prices',conn, if_exists='append', index=False)
    conn.close()
