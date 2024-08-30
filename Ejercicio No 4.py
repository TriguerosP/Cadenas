phone = input("Enter the phone number: ") 
parts = phone.split('-')  
number_without_prefix_and_extension = parts[1] if len(parts) > 2 else phone

print(f"The number without the prefix and extension is: {number_without_prefix_and_extension}")
