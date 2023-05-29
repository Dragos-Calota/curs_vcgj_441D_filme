from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/avatar/", methods=['GET'])
def getMovie():
    ret = "<h1>Avatar<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.getReleaseYear()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.getRating()
    ret += "<br>"

    
    
    
    
    return ret
    
@app.route("/avatar/year", methods=['GET'])
def getReleaseYearPage():
    ret = ""
    ret += lib.biblioteca_filme.getReleaseYear()
    
    return ret
    
@app.route("/avatar/rating", methods=['GET'])
def getRatingPage():
    ret = ""
    ret += lib.biblioteca_filme.getRating()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	
