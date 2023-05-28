from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/se7en/", methods=['GET'])
def get_tenet():
    ret = "<h1>Se7en<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_se7en()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_se7en()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/se7en/an_lansare", methods=['GET'])
def ia_an_lansare_tenet():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_se7en()
    
    return ret
    
@app.route("/se7en/rating", methods=['GET'])
def ia_rating_tenet():
    ret = ""
    ret += lib.biblioteca_filme.rating_se7en()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	


