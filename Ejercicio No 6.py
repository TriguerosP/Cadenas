phrase = input("Enter a phrase: ")
vocal = input("Enter a vocal: ")

modified_phrase = phrase.replace(vocal, vocal.upper())

print(f"The modified phrase is: {modified_phrase}")