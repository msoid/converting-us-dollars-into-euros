print("------Convert Dollars Into Euros------")
print("This program will help you convert any dollar amopunt into euros.")
print("Made by Tommy Bauer")


user_command = str(input("do you want to convert dollars into euros?: "))

def continue_user():
    user_dollar_amt = str(input("dollar amount to be converted: "))
    dollar = float(user_dollar_amt)
    euros = dollar*.94540
    print("your conversion total is:") 
    print(euros)
    


while user_command == "yes":
    continue_user()
    user_command = str(input("do you want to convert dollars into euros?: "))
    if user_command != "yes":
        break

        