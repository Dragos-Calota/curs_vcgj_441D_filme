import lib.biblioteca_filme as bfilme

def test_an_lansare_inglorious_basterds():
    var = bfilme.an_lansare_inglorious_basterds()
    if var == "2009" : 
        assert True
    else: 
        assert False
        

def test_rating_inglorious_basterds():
    var = bfilme.rating_inglorious_basterds()
    if var == "8.3" :
        assert True
    else: 
        assert False

