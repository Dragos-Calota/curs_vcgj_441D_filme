import lib.biblioteca_filme as bfilme

def test_an_lansare_inception():
    var = bfilme.an_lansare_inception()
    if var == "2010" : 
        assert True
    else: 
        assert False
        

def test_rating_inglorious_inception():
    var = bfilme.rating_inception()
    if var == "8.8" :
        assert True
    else: 
        assert False

