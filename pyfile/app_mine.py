from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/test")
def test_host():
    return '<p>test</p>'

@app.route("/input_num/<int:num>")
def input_num(num):
    return render_template('test_input.html', num=num)

@app.route("/sum_num")
def sum_num():
    n1 = request.args.get('a')
    n2 = request.args.get('b')
    n3 = int(n1) + int(n2)
    return render_template('sum_num_http.html', a=n1, b=n2, c=n3)

@app.route("/audio_play")
def audio_play():
    return render_template('audio_play.html')


@app.route("/")
def hello_world():
    if request.method == 'GET':
        return '<p>GET: Hello World</p>'
    elif request.method == 'POST':
        return '<p>POST: Hello World</p>'

def main():
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
