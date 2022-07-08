from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {
                "hello": "holse",
                "firework": "testFlask",
                "notDictionary": "isDictionary"
                }

def main():
    app.run(debug=True, host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()

