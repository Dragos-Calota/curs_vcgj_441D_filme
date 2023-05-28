import lib.biblioteca_filme 

def testReleaseYear():
    var = lib.biblioteca_filme.getReleaseYear()
    if var == "2012" : 
        assert True
    else: 
        assert False
        

def testRating():
    var = lib.biblioteca_filme.getRating()
    if var == "8.4" :
        assert True
    else: 
        assert False

