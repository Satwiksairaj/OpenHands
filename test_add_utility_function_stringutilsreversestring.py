import pytest
from add_utility_function_stringutilsreversestring import reverse_string

def test_reverse_string_normal():
    assert reverse_string("hello") == "olleh"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    assert reverse_string("x") == "x"