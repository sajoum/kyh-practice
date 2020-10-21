from uppg39 import calc_max, calculate_sum, multiply


def test_calc_max():
    expected = 3            #vad vi förväntar oss#
    got = calc_max(a=1, b=2, c=3)
    assert expected == got


def test_calculate_sum():
    got = calculate_sum([2, 2, 2])
    expected = 6
    assert expected == got


def test_multiply():
    got = multiply([2, 2, 2])
    expected = 8
    assert expected == got




