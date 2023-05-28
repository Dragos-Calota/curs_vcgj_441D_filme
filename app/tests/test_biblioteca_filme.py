import lib.biblioteca_filme as bfilme

def test_an_lansare_We_Bought_a_Zoo():
    var = bfilme.an_lansare_We_Bought_a_Zoo()
    if var == "2011" : 
        assert True
    else: 
        assert False
        

def test_rating_We_Bought_a_Zoo():
    var = bfilme.rating_We_Bought_a_Zoo()
    if var == "7.1" :
        assert True
    else: 
        assert False

