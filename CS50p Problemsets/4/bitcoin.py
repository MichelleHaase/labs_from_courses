import requests
import sys
import json

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    # print("Command-line argument is not a number")
    sys.exit("Command-line argument is not a number")
except IndexError:
    # print("Missing command-line argument")
    sys.exit("Missing command-line argument")

return_file = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# print(json.dumps(return_file.json()["bpi"]["USD"]["rate_float"]))
bitcoin = json.dumps(return_file.json()["bpi"]["USD"]["rate_float"])
# print(return_file.json())
# try:
#     ...
# except requests.RequestException:
#     ...

print(f"${(float(sys.argv[1])* float(bitcoin)):,.4f}")
