import lib.biblioteca_filme 

def test_releaseYear():
    var = lib.biblioteca_filme.get_an_lansare()
    if var == "2009" : 
        assert True
    else: 
        assert False
        

def test_rating():
    var = lib.biblioteca_filme.get_rating()
    if var == "8.3" :
        assert True
    else: 
        assert False
