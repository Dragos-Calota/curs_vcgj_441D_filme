from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/inception/", methods=['GET'])
def get_inception():
    ret = "<h1>Inception<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_inception()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_inception()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/inception/an_lansare", methods=['GET'])
def ia_an_lansare_inception():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_inception()
    
    return ret
    
@app.route("/inception/rating", methods=['GET'])
def ia_rating_inception():
    ret = ""
    ret += lib.biblioteca_filme.rating_inception()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	

