import lib.biblioteca_filme as bfilme

def test_an_lansare_Transporter():
    var = bfilme.an_lansare_Transporter()
    if var == "2002" : 
        assert True
    else: 
        assert False
        

def test_rating_Transporter():
    var = bfilme.rating_Transporter()
    if var == "6.8" :
        assert True
    else: 
        assert False

