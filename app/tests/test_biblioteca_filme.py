import lib.biblioteca_filme as bfilme

def test_an_lansare_titanic():
    var = bfilme.an_lansare_titanic()
    if var == "1997" : 
        assert True
    else: 
        assert False
        

def test_rating_titanic():
    var = bfilme.rating_titanic()
    if var == "7.9" :
        assert True
    else: 
        assert False


