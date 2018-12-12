#Requests Library

import requests

def main():
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    printResults(result)

    url = "http://httpbin.org/get"
    dataValues = {
        "k1":"v1",
        "k2": "v2",
        "k3": "v3"
    }
    result = requests.get(url, params = dataValues)
    printResults(result)

    url = "http://httpbin.org/post"
    result = requests.post(url, data=dataValues)
    printResults(result)

    #Custom Header
    url = "http://httpbin.org/get"
    headerValues = {
        "User-Agent" : "Joe Doe App / 1.0.0"
    }
    result = requests.get(url, headers=headerValues)
    printResults(result)


def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Headers: -------------------")
    print(resData.headers)
    print("\n")

    print("Returned Data: -------------------")
    #print(resData.content)
    print(resData.text)
    print("\n")

if __name__ == "__main__":
    main()

