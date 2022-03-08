from flask import Flask
import backend
app = Flask(__name__)
@app.route('/',methods=["GET"])
def getinfo():
    return backend.getinfo() 
if __name__ == "__main__":
        app.run(debug=True,port=8087,host="0.0.0.0")