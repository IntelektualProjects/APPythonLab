# modules
from WishList import WishList
from StockTracker import StockInfo

# Colors
red = "\u001b[31m"
yellow = "\u001b[33m"
white = "\u001b[37m"
blue = "\u001b[36m"
reset = "\u001b[0m"
green = "\u001b[32m"

user = input(f'''Welcome to {green}StockScan{reset}
Please register your name: ''')

while True:
    val = StockInfo().stock_info(user)
    if val != 0:
        pass

    while True:
        ans = input("Check another stock? (y/n): ")
        if ans in ('y', 'n'):
            break
        print("Invalid Input")
    if ans.lower() == 'y':
        continue
    else:
        break
