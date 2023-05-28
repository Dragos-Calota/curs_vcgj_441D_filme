from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/django/", methods=['GET'])
def get_tenet():
    ret = "<h1>Django Unchained<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_django()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_django()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/django/an_lansare", methods=['GET'])
def ia_an_lansare_django():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_django()
    
    return ret
    
@app.route("/django/rating", methods=['GET'])
def ia_rating_django():
    ret = ""
    ret += lib.biblioteca_filme.rating_django()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	

