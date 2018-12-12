#Basic Authentication

import requests
from requests.auth import HTTPBasicAuth

def main():
    url = "http://httpbin.org/basic-auth/JoeDoe/Password"
    myCreds = HTTPBasicAuth("Joe Doe","Password")
    result = requests.get(url, auth = myCreds)
    printResults(result)

def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Headers: -------------------")
    print(resData.headers)
    print("\n")

    print("Returned Data: -------------------")
    print(resData.text)
    print("\n")

if __name__ == "__main__":
    main()
