from flask import Flask

import lib.biblioteca

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/theirishman/", methods=['GET'])
def get_tenet():
    ret = "<h1>theirishman<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca.an_lansare_theirishman()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca.rating_theirishman()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/theirishman/an_lansare", methods=['GET'])
def ia_an_lansare_tenet():
    ret = ""
    ret += lib.biblioteca.an_lansare_theirishman()
    
    return ret
    
@app.route("/theirishman/rating", methods=['GET'])
def ia_rating_theirishman():
    ret = ""
    ret += lib.biblioteca.rating_theirishman()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	


