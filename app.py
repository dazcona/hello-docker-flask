from flask import Flask
 
app = Flask(__name__) 
 
@app.route('/')
def hello():
    return 'Hi from Docker & Flask with gunicorn!'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
