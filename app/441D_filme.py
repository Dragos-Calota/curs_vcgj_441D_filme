from flask import Flask
import biblioteca_filme

app = Flask(__name__)

print('441D_filme')

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre filme 441D</h1>"
    return ret

@app.route("/21/", methods=['GET'])
def get_21():
    ret = "<h1>21 Jump Street</h1>"
    ret += "An Lansare: "
    ret += biblioteca_filme.an_lansare_21()
    ret += "<br>"
    ret += "Rating IMDB: "
    ret += biblioteca_filme.rating_21()
    ret += "<br>"
    return ret

@app.route("/21/an_lansare", methods=['GET'])
def ia_an_lansare_21():
    ret = biblioteca_filme.an_lansare_21()
    return ret

@app.route("/21/rating", methods=['GET'])
def ia_rating_21():
    ret = biblioteca_filme.rating_21()
    return ret

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001)


