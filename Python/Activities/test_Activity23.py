import pytest

def test_sum_list(num_list):
    sum =0

    for n in num_list:
        sum = sum+n

    assert sum ==54