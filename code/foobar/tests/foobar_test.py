from src.main import foobar

def test_foobar_does_not_divide():
    assert foobar([1, 2, 7, 11, 13]) == []

def test_foobar_no_numbers():
    assert foobar([]) == []

def test_foobar_divides_by_three():
    assert foobar([6]) == ["foo"]

def test_foobar_divides_by_five():
    assert foobar([10]) == ["bar"]

def test_foobar_divides_by_five_and_three():
    assert foobar([30]) == ["foobar"]

def test_foobar_multiple():
    assert foobar([6, 3]) == ["foo", "foo"]

# def test_foobar_wrong_input():
#     assert foobar(["foo", "bar"])