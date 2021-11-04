from flask import Flask, render_template, request, redirect, session
import cx_Oracle
import requests


s = requests.session()
url = "http://www.in-sight.cn:6061/ords/ws001/dp/project_info/2019"
r = s.get(url)
result = r.json()['items']

qyxm = []
for item in result:
        dict = {
                'project_date': item.get("project_date"),
                'customer_name': item.get("customer_name"),
                'project_name': item.get("project_name"),
                'project_money': item.get("project_money")
        }
        qyxm.append(dict)
print(qyxm)
qyxm_dirt = {
        "rows": qyxm
}
