import biblioteca_filme as bfilme

def test_an_lansare_21():
    var = bfilme.an_lansare_21()
    if var == "2012" : 
        assert True
    else: 
        assert False
        

def test_rating_21():
    var = bfilme.rating_21()
    if var == "7.2" :
        assert True
    else: 
        assert False

