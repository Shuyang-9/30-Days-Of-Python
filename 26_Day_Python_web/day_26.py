from flask import Flask
import os

app = Flask(__name__)
@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# 导入flask
from flask import Flask
import os # 导入操作系统模块

app = Flask(__name__)

@app.route('/') # 这个装饰器创建主页路由
def home ():
    return '<h1>欢迎</h1>'

@app.route('/about')
def about():
    return '<h1>关于我们</h1>'

if __name__ == '__main__':
    # 部署时我们使用环境变量
    # 使其同时适用于生产和开发环境
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)