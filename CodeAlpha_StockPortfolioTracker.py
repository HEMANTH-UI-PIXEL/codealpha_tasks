# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 125,
    "MSFT": 310
}

portfolio = {}
total_value = 0

print("📊 Welcome to Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock symbol (AAPL/TSLA/GOOGL/AMZN/MSFT): ").upper()

    if stock not in stock_prices:
        print("❌ Invalid stock symbol! Please choose from the given list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

    choice = input("Do you want to add another stock? (yes/no): ").lower()
    if choice == "no":
        break

# Calculate total investment
print("\n🧮 Calculating total investment...\n")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print("\n💰 Total Portfolio Value:", total_value)

# Optional: Save to file
save_choice = input("\nWould you like to save this result as a .txt file? (yes/no): ").lower()

if save_choice == "yes":
    with open("stock_portfolio.txt", "w") as file:
        file.write("📊 Stock Portfolio Summary\n\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares × ₹{stock_prices[stock]} = ₹{stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Portfolio Value: ₹{total_value}\n")
    print("📁 File saved successfully as 'stock_portfolio.txt'")

print("\n✅ Program Finished — Thank You!")
