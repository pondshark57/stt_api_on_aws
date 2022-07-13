#flask import
from flask import  Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
#google api imprt
from google.cloud import speech
#
import io
import os

credential_path = "./google_stt_json_key/aws-stt-sever-project-3a48259ca53b.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

#flask module
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #flask json 형식에서 한글 깨짐 현상 해결

port_adress = "192.168.1.12"

word_array = [
    "아지매", "정구지", "정구지는", "어데서", "그라이께",
    "가마이", "쫌", "있으라", "안카더나", "와", "할배" ,
    "따갑거로", "하노", "촌시럽거로", "먼",
    "임마", "맞제", "이뻐예", "어데요", "아나",
    "니를", "내도", "내는", "아로", "비나",
    "하구로", "뽄때나게", "아이고", "알짱",
    "아이다", "진또배기", "인기라", "그마해라",
    "알라", "만키로", "뭇고", "문나", "왔노",
    "와그라노", "와이라노", "와그라는데", "와이라는데",
    "인자", "드가자", "퍼뜩", "됐다 그마해라"
]

@app.route('/')
def home_page():
    return render_template('upload.html')

@app.route('/file_upload', methods= ['GET', 'POST'])
def upload_audio():
    global port_adress

    if request.method == 'POST':

        #파일 저장 코
        f = request.files['file']
        #저장할 경로 + 파일명
        file_root = "./uploads/"+secure_filename(f.filename)
        f.save(file_root)

        #저장된 오디오 파일 stt api 적용
        result_text = stt_func(file_root)

        #나온 텍스트를 return
        return jsonify(text=result_text)

    elif request.method == 'GET':
        return render_template('upload.html')

#stt api module
client = speech.SpeechClient()
def stt_func(fileName):
    # The name of the audio file to transcribe
    file_name = fileName
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    global word_array
    cap_speech_context = speech.SpeechContext(phrases=word_array, boost=15)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        audio_channel_count=2,
        language_code='ko-KR',
        speech_contexts=[cap_speech_context]
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    result_text = []
    for result in response.results:
        result_text.append(result.alternatives[0].transcript)
        # print('Transcript: {}'.format(result.alternatives[0].transcript))
    print(result_text)
    return result_text[0]
    # [END speech_quickstart]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
