from typing import Set

from sys import maxunicode as sys_maxunicode


def get_all_supported_unicode_chars() -> Set[str]:
    supported_chars: Set[str] = set()
    code_point: int
    for code_point in range(1, sys_maxunicode):
        char: str = chr(code_point)
        supported_chars.update(char)

    return supported_chars
