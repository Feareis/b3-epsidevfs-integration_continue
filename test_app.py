# test_app.py
from app import convert_currency

def test_convert_currency():
    assert convert_currency(100, "USD", "EUR") == 94.89999999999999
