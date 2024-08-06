import requests
import json
import sys

def main():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        return

    dict1 = response.json()
    dict2 = dict1["bpi"]
    dict_USD = dict2["USD"]
    rate = float(dict_USD["rate"].replace(",", ""))

    inp = get_inp()
    out = float(inp * rate)
    print(out)

def get_inp():
    while True:
        try:
            inp = float(sys.argv[1])
            return inp
        except ValueError:
            sys.exit("0")
        except TypeError:
            sys.exit("1")
        except IndexError:
            sys.exit("Missing command-line argument")


main()
