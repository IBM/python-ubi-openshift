import os
import csv

# from errors.UserDefinedErrors import NotFoundError


def readData():
    """ for now we will hardcode this to read the ./data/countryCurrencyMetadata.csv """
    rows_ = []
    dir_path_ = os.path.dirname(os.path.realpath(__file__))
    file_path_ = "{}/data/countryCurrencyMetadata.csv".format(dir_path_)
    with open(file_path_, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows_.append(
                {
                    "country": row["country"],
                    "currencyName": row["currencyName"],
                    "currencyCode": row["currencyCode"],
                }
            )
    return rows_


def getCurrencyNameAndCode(countryName):
    data = readData()
    for row in data:
        if row["country"].upper() == countryName.upper():
            return row
    raise Exception("country {} does not exist".format(countryName))


def getCountryAndCurrencyCode(currencyCode):
    data = readData()
    if len(currencyCode.strip()) != 3:
        raise Exception("currencyCode should only be 3 characters long")
    matches = [v for v in data if v["currencyCode"].upper() == currencyCode.upper()]
    return {
        "currencyCode": matches[0]["currencyCode"],
        "currencyName": matches[0]["currencyName"],
        "country": [m["country"] for m in matches],
    }
