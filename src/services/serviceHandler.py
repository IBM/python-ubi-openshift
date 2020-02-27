from urllib.request import urlopen, Request  # noqa: 401
from urllib.error import HTTPError  # noqa: 401
import json
import logging

logger = logging.getLogger(__name__)

BASE_URL_ENDPOINT = "https://api.exchangeratesapi.io/"
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


class NotFoundException(Exception):
    pass


def __callExtRestEndPoint(url):
    request = Request(url)
    try:
        response = urlopen(request)
    except HTTPError as httpex:
        raise NotFoundException(httpex.reason)

    data = json.loads(response.read())
    return data


def getCurrencyExchangeRates(timeIndicator="latest"):
    currencyUrl = "{}{}".format(BASE_URL_ENDPOINT, timeIndicator)
    data = __callExtRestEndPoint(currencyUrl)
    return data


def getCurrencyExchangeRate(
    countryCurrencyCode, baseCode="EUR", timeIndicator="latest"
):

    countryCurrencyCode = countryCurrencyCode.upper()
    baseCode = baseCode.upper()

    currencyUrl = "{}{}?base={}".format(BASE_URL_ENDPOINT, timeIndicator, baseCode)
    data = __callExtRestEndPoint(currencyUrl)

    return data["rates"][countryCurrencyCode]


def convertCurrency(
    fromValue, fromCurrencyCode, toCurrencyCode, historicalDate="latest"
):
    exchangeRate = getCurrencyExchangeRate(
        toCurrencyCode, fromCurrencyCode, historicalDate
    )

    return fromValue * exchangeRate
