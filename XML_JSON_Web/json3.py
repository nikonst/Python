#JSON Exception Handling

import json
from json import JSONDecodeError

def main():

    jsonStr = '''{
                "sandwich": "Reuben",
                "toasted" : true,
                "toppings" : [
                    "Thousand Island Dressing",
                    "Sauerkraut",
                    "Pickles"
                ]
                "price" : 8.99
            }'''
    try:
        data = json.loads(jsonStr)
        print("Sandwich : " + data['sandwich'])
        if data['toasted']:
            print("It's toasted")
        for topping in data['toppings']:
            print("Topping " + topping)
    except JSONDecodeError as err:
        print("An Error occured :" + err.msg, err.lineno, err.colno)

if __name__ == "__main__":
    main()