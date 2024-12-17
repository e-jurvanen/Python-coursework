import requests
import sys

try:
    if len(sys.argv) == 2:
        bitcoin = float(sys.argv[1])
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        d = data.json()
        rate = float(d["bpi"]["USD"]["rate_float"])
        amount = bitcoin * rate
        print(f"${amount:,.4f}")
    elif len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    else:
        sys.exit("Command-line argument too long")

except ValueError:
    sys.exit("Comman-line argument is not a number")
except requests.RequestException:
    sys.exit("There has been a RequestException")
