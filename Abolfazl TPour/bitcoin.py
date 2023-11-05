import sys
import requests

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)
# Nested Dictionary
try:
    result = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    final_response = result.json()
    bitcoin_price = final_response["bpi"]["USD"]["rate_float"]
    total_price = bitcoin_price * value
    print(f"${total_price:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)