from flask import Flask
import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')

@app.route("/",methods=['GET'])
def index():
	ret = "<h1></h1>Informatii despre filme 441D</h1>"
	return ret

@app.route("/inglorious/", methods=['GET'])
def get_movie():
	ret = "<h1>Inglorious Basterds<h1>"
	ret += "An lansare: "
	ret += lib.biblioteca_filme.get_an_lansare()
	ret += "<br>"
	
	ret += "Rating IMDB: "
	ret += lib.biblioteca_filme.get_rating()
	ret += "<br>"
	
	return ret

@app.route("/inglorious/year", methods=['GET'])
def getYearPage():
	ret = ""
	ret += lib.biblioteca_filme.get_an_lansare()
	return ret
	
app.run(host = "127.0.0.1", port = 5001)
