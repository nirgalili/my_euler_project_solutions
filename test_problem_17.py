from problem_17 import Number, main


def test_number_construction():

    n = Number(5)
    assert n.letters_count_in_number==4


def test_main_10():
    res = main(10)
    assert res == 39

def test_main_20():
    res = main(20)
    assert res == 112

def test_main_30():
    res = main(30)
    assert res == 208

def test_main_40():
    res = main(40)
    assert res == 303

def test_main_1000():
    res = main(1000)
    assert res == 21124

