from flask import Flask
import json
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World V1!"

@app.route("/healthcheck")
def hello2():
    health = {'status': "Don't worry, I am running OK"}
    return json.dumps(health)
 
if __name__ == "__main__":
    app.run(port=5000,host='0.0.0.0')
