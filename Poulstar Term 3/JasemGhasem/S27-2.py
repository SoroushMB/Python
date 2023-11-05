# Function 
# def -> Define
# Variable : name = value
# Function : parameter = argument
def quarter(coin):
    return f"{int(coin/4)}¢"
coin = quarter(coin=100)
print(coin)