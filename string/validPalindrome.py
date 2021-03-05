"""
date : 2021/03/06
author : sehwa na
"""

import re


def is_valid_palindrome() -> bool:
    p1 = input()
    p2 = p1[::-1]

    p1 = re.sub("[^a-zA-Z0-9]", "", p1.lower())  # lower() -> 원본 리스트 변형 X
    p2 = re.sub("[^a-zA-Z0-9]", "", p2.lower())

    if p1 == p2:
        return True
    return False


print(is_valid_palindrome())
