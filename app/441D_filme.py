from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/Transporter/", methods=['GET'])
def get_Transporter():
    ret = "<h1>Transporter<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_Transporter()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_Transporter()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/Transporter/an_lansare", methods=['GET'])
def ia_an_lansare_Transporter():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_Transporter()
    
    return ret
    
@app.route("/Transporter/rating", methods=['GET'])
def ia_rating_Transporter():
    ret = ""
    ret += lib.biblioteca_filme.rating_Transporter()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	

