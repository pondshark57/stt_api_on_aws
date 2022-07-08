from flask import Flask, request

app = Flask(__name__)


@app.route("/test")
def r_test():
    return '<p>test</p>'


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return '<p>GET: Hello World</p>'
    elif request.method == 'POST':
        return '<p>POST: Hello World</p>'

def main():
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
