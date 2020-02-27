import pytest
from src.services.serviceHandler import convertCurrency, getCurrencyExchangeRates


@pytest.mark.xfail(raises=AssertionError)
def test_convertCurrency():
    countryCurrencyCode_ = "USD"
    expected_ = 13.313852615999998

    actual_ = convertCurrency(10, countryCurrencyCode_, "CAD")
    assert actual_ == expected_


@pytest.mark.xfail(raises=Exception)
def test_getEchangeRates():
    expected_ = {}
    actual_ = getCurrencyExchangeRates()
    assert actual_ == expected_
