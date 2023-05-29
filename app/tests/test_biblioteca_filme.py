import lib.biblioteca_filme 

def test_releaseYear():
    var = lib.biblioteca_filme.getReleaseYear()
    if var == "2009" : 
        assert True
    else: 
        assert False
        

def test_rating():
    var = lib.biblioteca_filme.getRating()
    if var == "7.9" :
        assert True
    else: 
        assert False

