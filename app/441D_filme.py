from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/Heat/", methods=['GET'])
def get_heat():
    ret = "<h1>Heat<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_heat()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_heat()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/heat/an_lansare", methods=['GET'])
def ia_an_lansare_heat():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_heat()
    
    return ret
    
@app.route("/heat/rating", methods=['GET'])
def ia_rating_heat():
    ret = ""
    ret += lib.biblioteca_filme.rating_heat()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	

