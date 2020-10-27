import requests


def checkIfUpdated():
    page = requests.get(
        'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3070/')

    return page.content


print(checkIfUpdated())
