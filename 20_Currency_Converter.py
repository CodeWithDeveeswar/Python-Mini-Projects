# Currency Converter (fixed rate)

rates = {"USD": 95, "EUR": 90, "GBP": 105}

amount = float(input("Amount in INR: "))
currency = input("Converted to (USD/EUR/GBP): ").upper()

converted = amount / rates[currency]

print(f"{amount} INR = {converted:.2f} {currency}")
