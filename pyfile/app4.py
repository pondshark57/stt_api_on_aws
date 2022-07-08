from flask import Flask, jsonify, request, render_template
app = Flask(__name__, static_url_path='../static') # 부트스트랩 파일 경로 path
@app.route('/login')
def login():
    email_address = request.args.get('email_address')
    passwd = request.args.get('passwd')
    print (passwd, email_address)
    if email_address == 'seungchan@abc.com':
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'failed'}
    return jsonify(return_data)
@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login_rawtest.html') # 부트스트랩 html파일
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")