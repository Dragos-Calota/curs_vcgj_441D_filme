from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/django/", methods=['GET'])
def getMovie():
    ret = "<h1>Django Unchained<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.getReleaseYear()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.getRating()
    ret += "<br>"

    ret += "Gen: "
    ret += lib.biblioteca_filme.getGenre()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/django/year", methods=['GET'])
def getReleaseYearPage():
    ret = ""
    ret += lib.biblioteca_filme.getReleaseYear()
    
    return ret
    
@app.route("/django/rating", methods=['GET'])
def getRatingPage():
    ret = ""
    ret += lib.biblioteca_filme.getRating()
    
    return ret
    
@app.route('/django/genre', methods=['GET'])
def getGenrePage():
    ret = ""
    ret += lib.biblioteca_filme.getGenre()

    



    
app.run(host = "127.0.0.1", port = 5001)	

