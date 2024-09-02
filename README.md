# Cryptocurrency-Portfolio-Tracker
The Cryptocurrency Portfolio Tracker is a Python-based application that allows users to monitor and manage their cryptocurrency investments.

# Code Overview
fetch_crypto_price(crypto_ids): Fetches the latest cryptocurrency prices using the CoinGecko API.

get_user_portfolio(): Prompts the user to input their cryptocurrency holdings and purchase prices.

calculate_portfolio_value(portfolio, prices): Calculates the current value of the portfolio and individual profit/loss.

plot_portfolio_distribution(portfolio, prices): Generates a pie chart showing the distribution of the user's cryptocurrency portfolio.

main(): Orchestrates the program's flow, integrating user input, API data retrieval, portfolio calculation, and visualization.

# Example Output
Bitcoin:
  Amount: 1.0
  Purchase Price: $26000.00
  Current Price: $57458.00
  Current Value: $57458.00
  Profit/Loss: $31458.00

Total Portfolio Value: $82000.00
