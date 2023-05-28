import lib.biblioteca as bfilme

def test_an_lansare_theirishman():
    var = bfilme.an_lansare_theirishman()
    if var == "2019" : 
        assert True
    else: 
        assert False
        

def test_rating_theirishman():
    var = bfilme.rating_theirishman()
    if var == "7.8" :
        assert True
    else: 
        assert False
