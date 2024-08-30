mail = input("Please enter email: ")
username, _ = mail.split('@')  
new_mail = username + '@ceu.es'  

print("Your new email is:", new_mail)