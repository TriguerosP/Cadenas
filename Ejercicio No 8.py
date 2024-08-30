price = input("Enter the price of the product in euros (with two decimal places): ")
euros, cents = price.split('.')

print(f"The price has {euros} euros and {cents} cents.")
