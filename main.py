from flask import Flask, render_template,url_for

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)