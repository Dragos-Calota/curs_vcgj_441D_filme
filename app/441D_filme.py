from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/LifeOfPi/", methods=['GET'])
def get_LifeOfPi():
    ret = "<h1>Life of Pi<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_LifeOfPi()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_LifeOfPi()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/LifeOfPi/an_lansare", methods=['GET'])
def ia_an_lansare_LifeOfPi():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_LifeOfPi()
    
    return ret
    
@app.route("/LifeOfPi/rating", methods=['GET'])
def ia_rating_LifeOfPi():
    ret = ""
    ret += lib.biblioteca_filme.rating_LifeOfPi()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	

