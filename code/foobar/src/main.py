def foobar(numbers):
    '''
    Returns foobar for 15, bar for 5, and foo for 3
    >>> foobar([3, 4, 5, 15])
    ['foo', 'bar', 'foobar']
    >>> foobar([3, 4, 5, 7])
    ['foo', 'bar']
    '''
    result = []
    for number in numbers:
        if number % 15 == 0:
            result.append("foobar")
        elif number % 3 == 0:
            result.append("bar")
        elif number % 5 == 0:
            result.append("bar")
    return result

if __name__ == '__main__':
    foo = "five"
    foo = 5
    numbers = input("Numbers?")
    print(foobar(numbers))

