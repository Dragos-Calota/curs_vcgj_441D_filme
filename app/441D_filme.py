from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/shooter/", methods=['GET'])
def get_shooter():
    ret = "<h1>shooter<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_shooter()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_shooter()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/shooter/an_lansare", methods=['GET'])
def ia_an_lansare_shooter():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_shooter()
    
    return ret
    
@app.route("/shooter/rating", methods=['GET'])
def ia_rating_shooter():
    ret = ""
    ret += lib.biblioteca_filme.rating_shooter()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	


