username = (input("Enter username: "))
password = (input("Enter password: "))

attempts = 1
while attempts < 5:
        if(username == "python") and (password == "rules"):
                print("Welcome")
                break
        else:
                print("Incorrect username or password. Please try again.")
                username = (input("Enter username: "))
                password = (input("Enter password: "))
                attempts = attempts + 1
if attempts == 5:
        print("Access denied")