import requests
import matplotlib.pyplot as plt

def fetch_crypto_price(crypto_ids):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(crypto_ids),
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_user_portfolio():
    portfolio = {}
    while True:
        crypto = input("Enter the cryptocurrency (eg. bitcoin) or 'done' to finish: ").lower()
        if crypto == 'done':
            break
        amount = float(input(f"Enter the amount of {crypto} you own: "))
        purchase_price = float(input(f"Enter the purchase price of {crypto} in USD: "))
        portfolio[crypto] = {
            'amount': amount,
            'purchase_price': purchase_price
        }
    return portfolio

def calculate_portfolio_value(portfolio, prices):
    total_value = 0
    for crypto, data in portfolio.items():
        current_price = prices[crypto]['usd']
        current_value = data['amount'] * current_price
        total_value += current_value
        print(f"{crypto.capitalize()}:")
        print(f"  Amount: {data['amount']}")
        print(f"  Purchase Price: ${data['purchase_price']:.2f}")
        print(f"  Current Price: ${current_price:.2f}")
        print(f"  Current Value: ${current_value:.2f}")
        print(f"  Profit/Loss: ${current_value - (data['amount'] * data['purchase_price']):.2f}\n")
    print(f"Total Portfolio Value: ${total_value:.2f}")
    return total_value

def plot_portfolio_distribution(portfolio, prices):
    labels = []
    values = []

    for crypto, data in portfolio.items():
        current_price = prices[crypto]['usd']
        current_value = data['amount'] * current_price
        labels.append(crypto.capitalize())
        values.append(current_value)

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Cryptocurrency Portfolio Distribution")
    plt.show()

def main():
    crypto_ids = []
    portfolio = get_user_portfolio()
    crypto_ids = list(portfolio.keys())
    prices = fetch_crypto_price(crypto_ids)
    
    if prices:
        calculate_portfolio_value(portfolio, prices)
        plot_portfolio_distribution(portfolio, prices)
    else:
        print("Error fetching prices. Please try again later.")

if __name__ == "__main__":
    main()