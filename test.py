import cx_Oracle

connection = cx_Oracle.connect('libin', 'admin123#', '127.0.0.1:1521/orcl')
cursor = connection.cursor()
ywnl = 'select c.customer_address,c.customer_industry,c.customer_name from customer_info c'
cursor.execute(ywnl)
ywnl_row = cursor.fetchall()
ywnl_list = []
for i in ywnl_row:
    dict = {
        'customer_address':i[0],
        'customer_industry':i[1],
        'customer_name':i[2]
    }
    ywnl_list.append(dict)
new_dirt = {
    "rows":ywnl_list
}
# print(new_dirt)
connection.close()



connection = cx_Oracle.connect('libin', 'admin123#', '127.0.0.1:1521/orcl')
cursor = connection.cursor()
khfb_map = 'select city_name,latitude,longitude from city_gps '
cursor.execute(khfb_map)
khfb_map_row = cursor.fetchall()
khfb_map_list = []
td = {}
for c,j,w in khfb_map_row:
    dict = {
           c:[j,w]
    }
    td.update(dict)
rd = {
    "gm_data":td
}

print(rd['gm_data'])
