#Send data to a server - GET and POST

import urllib.request
import urllib.parse

def main():
    url = "http://httpbin.org/get"

    args = {
        "name" : "Joe Doe",
        "isAuthor" : True
    }

    data = urllib.parse.urlencode(args)
    result = urllib.request.urlopen(url + "?" + data)

    print("Result code: {0}".format(result.status))
    print("Returned Data -----------------")
    print(result.read())

    url2 = "http://httpbin.org/post"
    data2 = data.encode()
    result2 = urllib.request.urlopen(url2, data = data2)

    print("Result code: {0}".format(result2.status))
    print("Returned Data -----------------")
    print(result2.read())

if __name__ == "__main__":
    main()
