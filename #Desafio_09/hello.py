from flask import Flask				# importa o flask

app = Flask(__name__)				# Inicia o Flask

# rotas basicas 

@app.route('/hello')						# atribui uma rota ao hello_world
def hello_world():
	return 'Hello World!!'

@app.route('/hi')						# atribui uma rota ao hi_world
def hi_world():
	return 'hi World!!'

@app.route('/day')						# atribui uma rota ao hi_world
def nice_day():
	return 'Have a nice day!!'

app.run()							# roda a aplicacao