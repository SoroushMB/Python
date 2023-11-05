from requests import get,RequestException
from sys import argv

try:
    bitprice = get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    final_price = float((bitprice["bpi"]["USD"]["rate"]).replace(",","")) * float(argv[1])
    print(f"${final_price:,}")
except IndexError:
    print("Missing command-line argument")
except ValueError:
    print("Command-line argument is not a number!")
except RequestException:
    print("Server isn't accessible!")