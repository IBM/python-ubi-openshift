from src.services import countryCurrencyCodeHandler

# from src.errors.UserDefinedErrors import NotFoundError
import pytest


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


def test_GetCurrencyNameAndCodeForNoCountry():
    with pytest.raises(Exception):
        countryCurrencyCodeHandler.getCurrencyNameAndCode("Westeros")


# there are 2 other ways to handle exceptions in pytest


# can mark a test with a python decorator that it will fail but that's OK it does as it should
@pytest.mark.xfail(raises=Exception)
def test_GetCurrencyNameAndCodeForNoCountryWithXfailMark():
    countryCurrencyCodeHandler.getCurrencyNameAndCode("Westeros")
