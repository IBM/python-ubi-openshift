import pytest
from src.services import countryCurrencyCodeHandler

def test_GetCurrencyNameAndCodeForRealCountry():
    expected_ = {
        "country": "South Africa",
        "currencyName": "South African rand",
        "currencyCode": "ZAR",
    }
    actual_ = countryCurrencyCodeHandler.getCurrencyNameAndCode("South Africa")
    assert actual_ == expected_


def test_GetSingleForRealCurrencyCode():
    currencyCode_ = "ZAR"
    expectedCountries_ = [
        "South Africa",
    ]

    expected_ = {
        "currencyCode": "ZAR",
        "currencyName": "South African rand",
        "country": expectedCountries_,
    }
    actual_ = countryCurrencyCodeHandler.getCountryAndCurrencyCode(currencyCode_)
    assert actual_ == expected_


def test_GetMultipleCountriesForRealCurrencyCode():
    currencyCode_ = "USD"
    expectedCountries_ = [
        "American Samoa",
        "Bonaire",
        "British Indian Ocean Territory",
        "British Virgin Islands",
        "Caribbean Netherlands",
        "Ecuador",
        "El Salvador",
        "Guam",
        "Marshall Islands",
        "Micronesia",
        "Northern Mariana Islands",
        "Palau",
        "Panama",
        "Puerto Rico",
        "Saba",
        "Sint Eustatius",
        "Timor-Leste",
        "Turks and Caicos Islands",
        "United States of America",
        "US Virgin Islands",
        "Wake Island",
        "Zimbabwe",
    ]

    expected_ = {
        "currencyCode": "USD",
        "currencyName": "United States dollar",
        "country": expectedCountries_,
    }
    actual_ = countryCurrencyCodeHandler.getCountryAndCurrencyCode(currencyCode_)
    assert actual_ == expected_


def test_CSV_to_Dict():
    """ we need a test to confirm we can read a csv and translate it into a useful python structure
    in this case a list of dict rows"""
    expected_ = {
        "country": "Zimbabwe",
        "currencyCode": "USD",
        "currencyName": "United States dollar",
    }

    actual_ = countryCurrencyCodeHandler.readData()
    assert actual_[-1] == expected_
    assert len(actual_) == 253

# there are 2 ways to handle exceptions in the Pytest framework
# 1. hanlde the exception in the test
def test_GetCurrencyNameAndCodeForNoCountry():
    with pytest.raises(Exception):
        countryCurrencyCodeHandler.getCurrencyNameAndCode("Westeros")


# 2. mark the test with a python decorator 
# that will fail by design 
# this means the test should PASS ( even with Travis/CircleCI/Jenkins etc)
@pytest.mark.xfail(raises=Exception)
def test_GetCurrencyNameAndCodeForNoCountryWithXfailMark():
    countryCurrencyCodeHandler.getCurrencyNameAndCode("Westeros")
