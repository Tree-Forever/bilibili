from flask import Flask,  render_template, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('post.html')

@app.route('/server', methods=['GET','POST'])
def index():
    resp = make_response("HELLO WORLD", 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'    #允许跨域
    return resp

if __name__ == '__main__':
    app.run()
