from flask import Flask
from flask import jsonify
import os

## create new app
app = Flask(__name__)
#lets create new route
@app.route('/')
#now we will create a new function
def dir():
    #this function will fetch all items in a foder/directory
    all = os.listdir('templates')
    return jsonify(all)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
#Let run over app. I am using port 8080. by default it is 5000.