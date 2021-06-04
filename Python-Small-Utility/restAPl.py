from flask import Flask, jsonify
from ArmstrongNumber import armstrong
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/armstrong/<string:n>')
def arm(n):
    return jsonify(armstrong(n))

if __name__ == '__main__':
    app.run(debug=True)