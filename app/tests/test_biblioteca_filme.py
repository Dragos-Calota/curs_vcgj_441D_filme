import lib.biblioteca_filme 

def test_releaseYear():
    var = lib.biblioteca_filme.getReleaseYear()
    if var == "2012" : 
        assert True
    else: 
        assert False
        

def test_rating():
    var = lib.biblioteca_filme.getRating()
    if var == "8.4" :
        assert True
    else: 
        assert False

def test_genre():
    var = lib.biblioteca_filme.getGenre()
    if var == 'Western':
        assert True
    else:
        assert False