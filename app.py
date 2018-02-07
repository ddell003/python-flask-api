#!flask/bin/python
from flask import Flask

app = Flask(_name_)

@app.route('/')
def index():
	return "Hello, world!"

if __name__ == '__main__':
	app.run(debug=True)
