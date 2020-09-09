import pyodbc
import random

server = 'servername.westus2.cloudapp.azure.com'
database = ''
username = ''
password = ''
conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + \
    server+';DATABASE='+database+';UID='+username+';PWD=' + password


def get_some_data():
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()

    result_list = []
    
    query_one = cursor.execute("""
                                select top 50 column1, column2, column3
                                from dbo.some_table dm
                                where column1 = 2 
                                """)

    for row in query_one:
        result_dict = {'column1': row[0],
                       'column2': row[1], 'column3': row[2]}
        result_list.append(result_dict)
 
    random.shuffle(result_list)

    return result_list


def insert_some_info(data):
    pass
    try:
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("""
                        INSERT INTO dbo.some_table column1, column2, column3) 
                        VALUES(?,?,?)
                        """,
                       (data['column1'], data['column2'], data['column3']))
        conn.commit()
    except:
        pass


def update_some_data(data):
    try:
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("""
                        update tblDomainMerchants
                        set column1 = ?
                        where column2 = ?
                        """,
                       (data['column1'], data['column1']))
                       
        conn.commit()
        conn.close
    except Exception as e:
        print(e)
        pass