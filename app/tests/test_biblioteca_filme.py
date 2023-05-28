import lib.biblioteca_filme as bfilme

def test_an_lansare_se7en():
    var = bfilme.an_lansare_se7en()
    if var == "1995" : 
        assert True
    else: 
        assert False
        

def test_rating_se7en():
    var = bfilme.rating_se7en()
    if var == "8.6" :
        assert True
    else: 
        assert False


