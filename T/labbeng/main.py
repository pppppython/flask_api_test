import os
from flask import render_template,url_for,request,Blueprint,Response
import json

main_bp=Blueprint('main',__name__) #定义蓝本

@main_bp.route('/',methods=['GET'])
def a():
    return render_template('a.html')

@main_bp.route('/login',methods=['GET','POST'])
def login():
    print(request.method)
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    return {'name': 'letian', 'password': '123'}


