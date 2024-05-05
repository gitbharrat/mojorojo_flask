from square import square


def test_square():          # Unit Testing
    n = 4
    result = square(n)
    assert result == 16


if __name__ == '__main__':
    test_square()
