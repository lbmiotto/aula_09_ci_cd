import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    n1 = 3
    n2 = 4

    output = methods.soma(n1, n2)

    assert output == 7

def test_subtracao():
    n1 = 6
    n2 = 5

    output = methods.subtracao(n1, n2)

    assert output == 1

def test_divisao():
    n1 = 10
    n2 = 5

    output = methods.divisao(n1, n2)

    assert output == 2

def test_multiplicacao():
    n1 = 6
    n2 = 10

    output = methods.multiplicacao(n1, n2)
    
    assert output == 60
