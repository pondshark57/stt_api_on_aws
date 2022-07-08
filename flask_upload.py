from flask import  Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/file_upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #request.headers['x-api-key'] = "NQQER6KDC5ROU3TO4GJVBJVIJA3EK62C"
        f = request.files['file']
        #저장할 경로 + 파일명
        f.save("./uploads/" + secure_filename(f.filename))
        return 'uploads 디렉토리 -> 파일업로드 성공!'
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)