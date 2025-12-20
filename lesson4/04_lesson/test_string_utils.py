import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitalize_positive(string_utils):
    assert string_utils.capitalize("привет") == "Привет"
    assert string_utils.capitalize("Привет") == "Привет"
    assert string_utils.capitalize("п") == "П"

def test_capitalize_negative(string_utils):
    assert string_utils.capitalize("привет") != "привет"
    assert string_utils.capitalize("ЛЮДИ") != "люди"

def test_trim_positive(string_utils):
    assert string_utils.trim("     привет") == "привет"
    assert string_utils.trim("привет") == "привет"
    
def test_trim_negative(string_utils):
    assert string_utils.trim("привет     ") == "привет     "
    assert string_utils.trim("     Привет            народ") == "Привет            народ"

def test_contains_positive(string_utils):
    assert string_utils.contains("Домашняя работа", "р") is True
    assert string_utils.contains("привет люди", "рив") is True

def test_contains_negative(string_utils):
    assert string_utils.contains("Домашняя работа", "з") is False
    assert string_utils.contains("hello", "z") is False

def test_contains_edge_cases(string_utils):
    assert string_utils.contains("", "a") is False
    assert string_utils.contains("привет", "") is True  

def test_delete_symbol_positive(string_utils):
    result = string_utils.delete_symbol("Домашняя работа", "а")
    assert result == "Домшняя рбот"

    result = string_utils.delete_symbol("привет люди", "рив")
    assert result == "пет люди"

def test_delete_symbol_negative(string_utils):
    original = "привет"
    assert string_utils.delete_symbol(original, "z") == original

def test_delete_symbol_edge_cases(string_utils):
    assert string_utils.delete_symbol("", "a") == ""

    
    result = string_utils.delete_symbol("все", "")
    assert result == "все"  
