import lib.biblioteca_filme as bfilme

def test_an_lansare_shooter():
    var = bfilme.an_lansare_shooter()
    if var == "2007" : 
        assert True
    else: 
        assert False
        

def test_rating_shooter():
    var = bfilme.rating_shooter()
    if var == "7.1" :
        assert True
    else: 
        assert False

