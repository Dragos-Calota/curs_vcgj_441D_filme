from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/shutter/", methods=['GET'])
def get_film():
    ret = "<h1>Shutter Island<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/shutter/an_lansare", methods=['GET'])
def ia_an_lansare():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare()
    
    return ret
    
@app.route("/shutter/rating", methods=['GET'])
def ia_rating():
    ret = ""
    ret += lib.biblioteca_filme.rating()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	


