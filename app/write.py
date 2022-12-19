def load_db_table(df, conn, table_name, key):
    min_key = df[key].min()
    max_key = df[key].max()
    df.to_sql(table_name, conn, if_exists='append', index=False)
    print(f'Loaded data for {table_name} within the range of {min_key} and {max_key}')



if __name__ == '__main__':
    import pandas as pd
    import os
    df = 'a'
    conn = 'Docker exec -it retail psql -U retail_user -d retail_db'
    load_db_table(df, conn, 'users','user_id')

