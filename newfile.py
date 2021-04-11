from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/a/<int:n>')
def myfun(n):
    n={
    "name":"joh",
    "class":n
    }
    
    return jsonify(n)
 
    
    
if __name__ == "__main__":
	app.run(debug=True)
	
	