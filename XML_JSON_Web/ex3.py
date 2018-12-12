#Handling errors

import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError

def main():
    url = "http://no-server.org" #URL Error
    #url = "http://httpbin.org/status/404" # HTTP Error
    #url = "http://httpbin.org/get"

    try:
        result = urllib.request.urlopen(url)
        print("Result code: {0}".format(result.status))
        #if result.getcode() == 200:
        if result.getcode() == HTTPStatus.OK:
            print("Returned Data -----------------")
            print(result.read())
    except HTTPError as err:
        print("Error {0}".format(err.code))
    except URLError as err:
        print("What a server! {0}".format(err.reason))

if __name__ == "__main__":
    main()
