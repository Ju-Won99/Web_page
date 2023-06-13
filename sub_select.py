from flask import Flask,request
import pyodbc

app = Flask(__name__)
def connection():
    s = 'IP,port_Number'
    d = 'DB(company_Name)'
    u = 'DB_ID'
    p = 'DB_PassWord'
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+p+';'
    conn = pyodbc.connect(cstr)
    return conn

def get_all_data():
    storage = request.args.get('')
    conn = connection()
    cursor = conn.cursor()
    cmd_prod_executesp1 = """
    DECLARE @return_value int
    EXEC    @return_value = [dbo].[USP_ASS_L]
            @P_VALUE1 = ?
    SELECT 'Return Value' = @return_value
    """
    params = (storage)
    cursor.execute(cmd_prod_executesp1, params)
    
    
    all_data = []

    try:
        for row in cursor:
            all_data.append(row)
            if cursor.nextset():
                all_data = cursor.fetchall()
    except Exception as e:
        app.logger.error("예외가 발생했습니다: %s", e)
        conn.close()
        return None
    conn.close()

    return all_data

def get_unique_ids(data):
    unique_ids = set()
    for row in data:
        if row.WH_ID:
            unique_ids.add(row.WH_ID)
    return sorted(unique_ids)
