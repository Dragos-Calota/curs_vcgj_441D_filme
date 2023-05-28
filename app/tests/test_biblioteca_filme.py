import lib.biblioteca_filme as bfilme

def test_an_lansare_CompletNecunoscuti():
    var = bfilme.an_lansare_CompletNecunoscuti()
    if var == "2021" : 
        assert True
    else: 
        assert False
        

def test_rating_CompletNecunoscuti():
    var = bfilme.rating_CompletNecunoscuti()
    if var == "7.9" :
        assert True
    else: 
        assert False


