from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/TheRevenant/", methods=['GET'])
def get_TheRevenant():
    ret = "<h1>TheRevenant<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_TheRevenant()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_TheRevenant()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/TheRevenant/an_lansare", methods=['GET'])
def ia_an_lansare_TheRevenant():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_TheRevenant()
    
    return ret
    
@app.route("/TheRevenant/rating", methods=['GET'])
def ia_rating_TheRevenant():
    ret = ""
    ret += lib.biblioteca_filme.rating_TheRevenant()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	

