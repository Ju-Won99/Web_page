from flask import Flask, render_template,request
from flask_paginate import Pagination
import pyodbc
import sub_select

app = Flask(__name__)

def connection():
    s = '192.168.1.230,3103'
    d = 'BODITECH_MES'
    u = 'geust_01'
    p = 'choi990$%^'
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+p+';'
    conn = pyodbc.connect(cstr)
    return conn


@app.route("/", methods=['GET','POST'])

def main():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    try:
        page = int(request.args.get('page',1))
    except:
        page = 1 
    storage = request.args.get('storage')
    num = request.args.get('num')
    Lot_No = request.args.get('Lot_No')
    P_Name = request.args.get('P_Name')
    conn = connection()
    cursor = conn.cursor()
    cmd_prod_executesp1 = """
    DECLARE @return_value int
    EXEC    @return_value = [dbo].[USP_ASS_L]
            @P_VALUE1 = ?,
            @P_VALUE2 = ?,
            @P_VALUE3 = ?,  
            @P_VALUE4 = ?
    SELECT 'Return Value' = @return_value
    """
    params = (storage, num, Lot_No, P_Name)
    cursor.execute(cmd_prod_executesp1, params)
    
    PER_PAGE = int(request.args.get('per_page', 10))
    lists = []
    try:
        
        for row in cursor:
            lists.append(row) 
            if cursor.nextset():            # 2번 째 resultset으로 이동
                lists = cursor.fetchall()   # 2번 쨰 resultset의 전체 출력
                total = len(lists)          # 나온 결과 셋의 길이
                i = (page-1)*PER_PAGE       # 시작 인덱스 계산
                List1 = lists[i:i+PER_PAGE]   
                pagination = Pagination(page=page, per_page=PER_PAGE,total=total, search=search)
                
    except Exception as e:
        app.logger.error("예외가 발생했습니다: %s", e)
        conn.close()
        return "An error occured while processing the data."
    conn.close()

    unique_ids = sub_select.get_unique_ids(sub_select.get_all_data())
    return render_template('main/list.html', lists=List1,unique_ids=unique_ids, pagination=pagination,total = total, bs_version=5)


print(pyodbc.drivers())

if(__name__ == "__main__"):
    app.run()
