#performing flask imports
from flask import Flask,jsonify,request
import test

app = Flask(__name__) #intance of our flask application 

#Route '/' to facilitate get request from our flutter app
@app.route('/api', methods=['GET'])
def index():
    print(request)
    sl = str(request.args['sl'])
    z=test.get_bio(sl)
    return jsonify({'greetings' : z}) #returning key-value pair in json format


if __name__ == "__main__":
    app.run(debug = True) #debug will allow changes without shutting down the server 

