import lib.biblioteca_filme as bfilme

def test_an_lansare_LifeOfPi():
    var = bfilme.an_lansare_LifeOfPi()
    if var == "2012" : 
        assert True
    else: 
        assert False
        

def test_rating_LifeOfPi():
    var = bfilme.rating_LifeOfPi()
    if var == "7.9" :
        assert True
    else: 
        assert False

