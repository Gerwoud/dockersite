import requests

def get():
    response = requests.get("https://volleybieb.be/ajax/ajaxVVBWedstijden.php?wattedoen=1&provincie=6&reeks=OHP3&competitie=100&team=0&stamnummer=O-1283")
    data = response.json()
    # print(data)
    matchen = []
    for x in data:
        if x["thuisploeg"] == "Volley Team TEMSE B" or x["bezoekers"] == "Volley Team TEMSE B":
            # print(x)
            del x['myOK']
            del x['mySql']
            matchen.append(x)

    print(len(matchen))
    print(matchen)

    return matchen

if __name__ == '__main__':
    get()