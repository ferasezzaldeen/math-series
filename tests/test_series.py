
from math_series.series import fibonacci,lucas,sum_series

def test_fibonacci():
    expected={
        0:0,
        1:1,
        2:1,
        3:2,
        4:3,
    }
    actual=fibonacci(expected)

    assert expected==actual

def test_lucas():
    expected={
        0:2,
        1:1,
        2:3,
        3:4,
        4:7,
    }
    actual=lucas(expected)

    assert expected==actual

def test_sum():
    expected={
    0:0,
    1:1,
    2:1,
    3:2,
    4:3
    }
    actual=sum_series(expected)
    assert expected==actual
