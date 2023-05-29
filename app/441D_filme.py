from flask import Flask

import lib.biblioteca_filme

app = Flask(__name__)

print('441D_filme')


@app.route("/" ,methods=['GET'])
def index():
    ret="<h1></h1>Informatii despre filme 441D</h1>"
    return ret
    
@app.route("/CompletNecunoscuti/", methods=['GET'])
def get_CompletNecunoscuti():
    ret = "<h1>CompletNecunoscuti<h1>"
    ret += "An Lansare: "
    ret += lib.biblioteca_filme.an_lansare_CompletNecunoscuti()
    ret += "<br>"
    
    ret += "Rating IMDB: "
    ret += lib.biblioteca_filme.rating_CompletNecunoscuti()
    ret += "<br>"
    
    
    
    return ret
    
@app.route("/CompletNecunoscuti/an_lansare", methods=['GET'])
def ia_an_lansare_CompletNecunoscuti():
    ret = ""
    ret += lib.biblioteca_filme.an_lansare_CompletNecunoscuti()
    
    return ret
    
@app.route("/CompletNecunoscuti/rating", methods=['GET'])
def ia_rating_CompletNecunoscuti():
    ret = ""
    ret += lib.biblioteca_filme.rating_CompletNecunoscuti()
    
    return ret
    

    



    
app.run(host = "127.0.0.1", port = 5001)	


