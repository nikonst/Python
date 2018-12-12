import json

def main():
    pythonData = {
                "sandwich" : "Reuben",
                "toasted" : True,
                "toppings" : [
                    "Thousand Island Dressing",
                    "Sauerkraut",
                    "Pickles"
                ],
                "price" : 8.99
            }

    jsonStr = json.dumps(pythonData, indent = 4)
    print("JSON Data:")
    print(jsonStr)

if __name__ == "__main__":
    main()