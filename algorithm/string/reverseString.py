"""
date : 2021/03/06
author : sehwa na
reference : 파이썬 알고리즘 인터뷰
"""


def reverse_string_using_reverse_function(arr: list) -> list:
    arr.reverse()
    return arr


def reverse_string_using_slicing(arr: list) -> list:
    return arr[::-1]


print(reverse_string_using_reverse_function(["h", "e", "l", "l", "o"]))
print(reverse_string_using_slicing(["h", "e", "l", "l", "o"]))