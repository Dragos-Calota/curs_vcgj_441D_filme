from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/titanic/", methods=['GET'])
def get_titanic():
    ret = "<h1>Titanic<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_titanic()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_titanic()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/titanic/an_lansare", methods=['GET'])
def ia_an_lansare_titanic():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_titanic()
    
    return ret
    
@app.route("/titanic/rating", methods=['GET'])
def ia_rating_titanic():
    ret = ""
    ret += lib.biblioteca_filme.rating_titanic()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	


