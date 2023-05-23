import lib.biblioteca_filme as bfilme

def test_an_lansare_tenet():
    var = bfilme.an_lansare_tenet()
    if var == "2020" : 
        assert True
    else: 
        assert False
        

def test_rating_tenet():
    var = bfilme.rating_tenet()
    if var == "7.3" :
        assert True
    else: 
        assert False


