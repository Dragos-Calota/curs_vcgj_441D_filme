from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/baywatch/", methods=['GET'])
def get_baywatch():
    ret = "<h1>Baywatch<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_baywatch()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_baywatch()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/baywatch/an_lansare", methods=['GET'])
def ia_an_lansare_baywatch():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_baywatch()
    
    return ret
    
@app.route("/baywatch/rating", methods=['GET'])
def ia_rating_baywatch():
    ret = ""
    ret += lib.biblioteca_filme.rating_baywatch()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	



