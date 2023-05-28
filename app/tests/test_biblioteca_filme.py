import lib.biblioteca_filme as bfilme

def test_an_lansare_heat():
    var = bfilme.an_lansare_heat()
    if var == "1995" : 
        assert True
    else: 
        assert False
        

def test_rating_heat():
    var = bfilme.rating_heat()
    if var == "8.3" :
        assert True
    else: 
        assert False
