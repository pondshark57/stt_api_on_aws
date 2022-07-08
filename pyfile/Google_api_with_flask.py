import speech_recognition as sr
from flask import Flask, render_template, request, redirect

def micro_response():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio=r.listen(source)

    try:
        transcript=r.recognize_google(audio, language="ko-KR")
        print("Google Speech Recognition thinks you said "+transcript)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
