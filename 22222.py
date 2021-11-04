import requests,json
import cx_Oracle


connection = cx_Oracle.connect('libin', 'admin123#', '127.0.0.1:1521/orcl')
cursor = connection.cursor()
qyxm = 'select a.project_date,a.customer_name,a.project_name,a.project_money from project_info a'
cursor.execute(qyxm)
qyxm_row = cursor.fetchall()
qyxm_row_date = []
for item in qyxm_row:
    dict = {
        'project_date': item[0],
        'customer_name': item[1],
        'project_name': item[2],
        'project_money': item[3],
    }
    qyxm_row_date.append(dict)
qyxm_dirt = {
    "rows": qyxm_row_date
}
print(qyxm_dirt)
connection.close()
