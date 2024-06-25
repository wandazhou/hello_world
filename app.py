#导入Flask类
from flask import Flask
#实例化,可视为固定格式
app = Flask(__name__)
#route()方法用于设定路由,网址后半部分
@app.route('/helloworld')
def hello_world():
    #打开网址呈现的内容：Hello,World!
    return 'Hello, World!'
#固定格式执行main
if __name__ == '__main__':
    #app.run(host, port, debug, options)
    app.run(host="0.0.0.0", port=5001)
   #默认值：host="127.0.0.1", port=5000, debug=False，
   #即本机ip，于是访问网址为：http://127.0.0.1:5000/helloworld
