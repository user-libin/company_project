from flask import Flask, render_template, request, redirect, session
import cx_Oracle

app = Flask(__name__)
app.secret_key = 'qwert'

#数据连接
# 业务规模-签约合同金额
connection = cx_Oracle.connect('libin', 'admin123#', '127.0.0.1:1521/orcl')
cursor = connection.cursor()
cursor.execute('select project_date,project_money from project_info')
qyhtje_row = cursor.fetchall()
qyhtje_row_x = []
qyhtje_row_y = []
for i in qyhtje_row:
    qyhtje_row_x.append(i[0])
    qyhtje_row_y.append(i[1])
connection.close()


# 业务规模-签约项目
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
connection.close()


# 客户分布-项目概况
connection = cx_Oracle.connect('libin', 'admin123#', '127.0.0.1:1521/orcl')
cursor = connection.cursor()
xmgk = 'select c.customer_address,c.customer_industry,c.customer_name from customer_info c'
cursor.execute(xmgk)
xmgk_row = cursor.fetchall()
xmgk_row_date = []
for item in xmgk_row:
    dict = {
        'customer_address': item[0],
        'customer_industry': item[1],
        'customer_name': item[2],
    }
    xmgk_row_date.append(dict)
xmgk_dirt = {
    "rows": xmgk_row_date
}
connection.close()


# 客户分布-地图gps
connection = cx_Oracle.connect('libin', 'admin123#', '127.0.0.1:1521/orcl')
cursor = connection.cursor()
khfb_map = 'select city_name,latitude,longitude from city_gps '
cursor.execute(khfb_map)
khfb_map_row = cursor.fetchall()
khfb_map_list = {}
for c, j, w in khfb_map_row:
    dict = {
        c: [j, w]
    }
    khfb_map_list.update(dict)
connection.close()


# 客户分布-地图data
connection = cx_Oracle.connect('libin', 'admin123#', '127.0.0.1:1521/orcl')
cursor = connection.cursor()
khfb_map_daat = 'select distinct(customer_address),20 as value from customer_info'
cursor.execute(khfb_map_daat)
khfb_map_data_row = cursor.fetchall()
khfb_map_data_list = []
for i in khfb_map_data_row:
    dict = {
        'name': i[0],
        'value': i[1]
    }
    khfb_map_data_list.append(dict)
connection.close()



# 登录管理
@app.route('/', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    if username and password:
        if username == 'admin' and password == 'admin123':  #用户名密码
            session['username'] = username
            session['password'] = password
            print("用户登录成功")
        else:
            print("用户密码错误")

# 定义不同用户访问不同页面
    if username == 'admin' and password == 'admin123':
        return render_template('index.html', username=username)
    # 普通用户访问页面
    elif username == 'libin' and password == 'admin123':
        return render_template('kehufenbu.html', username=username)
    else:
        return render_template('login.html', error_msg="用户或密码错误")


@app.route('/logout', methods=['GET'])
def logout():
    # 清除session缓存
    session.clear()
    print("退出登录用户", session)
    return redirect('/')


# 管理员用户
@app.route('/index')
def index():
    if 'username' in session and 'password' in session:
        return render_template('index.html', username=session['username'])
    else:
        return render_template('login.html')


@app.route('/kehufenbu')
def kehufenbu():
    return render_template('kehufenbu.html', username=session['username'])


# 数据调用
# 业务规模数据
@app.route('/ywgm', methods=['GET', 'POST'])
def ywgm():
    json_data = {
        "title": '签约合同金额',
        "x_data": qyhtje_row_x,
        "s_data": qyhtje_row_y
    }
    return json_data


# 签约项目
@app.route('/qyxm', methods=['GET', 'POST'])
def qyxm():
    return qyxm_dirt


# 客户分布
@app.route('/khfb', methods=['GET', 'POST'])
def khfb():
    json_data = {
        "m_data": khfb_map_data_list,
        # "m_data":
        #     [{
        #                 "name": '哈尔滨',
        #                 "value": 20
        #             },
        #             {
        #                 "name": '长春',
        #                 "value": 20
        #             },
        #         ],
        "gm_data": khfb_map_list
        #     {
        #     '哈尔滨': [126.6433411, 45.74149323],
        #     '长春': [125.3154297, 43.89256287],
        #     '呼和浩特': [111.6632996, 40.82094193]
        # },
    }
    return json_data


# 项目概况
@app.route('/xmgk', methods=['GET', 'POST'])
def xmgk():
    return xmgk_dirt


if __name__ == '__main__':
    app.run()
